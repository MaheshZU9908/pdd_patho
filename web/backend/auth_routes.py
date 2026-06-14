from fastapi import APIRouter, Depends, HTTPException, status, Request, Response, Header
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta, datetime

from .database import get_db
from . import models, auth, mfa
from pydantic import BaseModel, EmailStr
import base64

router = APIRouter(prefix="/auth", tags=["auth"])


# ── Schemas ────────────────────────────────────────────────────────────────────
class RegisterSchema(BaseModel):
    email: EmailStr
    password: str
    full_name: str = ""
    institution: str = ""
    license_id: str = ""


class ResetPasswordSchema(BaseModel):
    token: str
    new_password: str


class EnableMFASchema(BaseModel):
    code: str


class ForgotPasswordSchema(BaseModel):
    email: EmailStr


# ── Helpers ────────────────────────────────────────────────────────────────────
def send_reset_email(email: str, token: str):
    reset_link = f"http://localhost:8000/reset-password?token={token}"
    print(f"[Email] To: {email}\nSubject: PathoAI Password Reset\nReset link: {reset_link}\n")


def _get_current_user_from_request(request: Request, db: Session):
    token = request.cookies.get("access_token") or (
        request.headers.get("Authorization", "").replace("Bearer ", "").strip() or None
    )
    if not token:
        raise HTTPException(status_code=401, detail="Not authenticated")
    payload = auth.decode_access_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token")
    user = db.query(models.User).filter(models.User.id == int(payload["sub"])).first()
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    return user


# ── Routes ─────────────────────────────────────────────────────────────────────
@router.post("/register", status_code=status.HTTP_201_CREATED)
def register(data: RegisterSchema, db: Session = Depends(get_db)):
    existing = db.query(models.User).filter(models.User.email == data.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed = auth.get_password_hash(data.password)
    totp_secret = mfa.generate_totp_secret()
    uri = mfa.get_totp_uri(totp_secret, data.email)
    qr_data_uri = mfa.generate_qr_code_data_uri(uri)
    user = models.User(
        email=data.email,
        hashed_password=hashed,
        full_name=data.full_name,
        institution=data.institution,
        license_id=data.license_id,
        totp_secret=totp_secret,
        mfa_enabled=False,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return {
        "msg": "User registered successfully",
        "qr_code": qr_data_uri,
        "mfa_enabled": False,
    }


@router.post("/login")
def login(
    response: Response,
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
    totp_code: str = Header(None, alias="X-TOTP"),
):
    user = db.query(models.User).filter(models.User.email == form_data.username).first()
    if not user or not auth.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    if user.mfa_enabled:
        if not totp_code:
            raise HTTPException(status_code=401, detail="MFA code required")
        totp = mfa.totp_from_secret(user.totp_secret) if hasattr(mfa, "totp_from_secret") else None
        if totp and not totp.verify(totp_code):
            raise HTTPException(status_code=401, detail="Invalid MFA code")
    access_token = auth.create_access_token({"sub": str(user.id)})
    response.set_cookie(
        key="access_token", value=access_token,
        httponly=True, max_age=60 * 60 * 24,  # 24 h
        samesite="lax",
    )
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": {
            "id": user.id,
            "email": user.email,
            "full_name": user.full_name,
            "institution": user.institution,
            "mfa_enabled": user.mfa_enabled,
        },
    }


@router.post("/logout")
def logout(response: Response):
    response.delete_cookie(key="access_token")
    return {"msg": "Logged out"}


@router.get("/me")
def read_me(request: Request, db: Session = Depends(get_db)):
    user = _get_current_user_from_request(request, db)
    return {
        "id": user.id,
        "email": user.email,
        "full_name": user.full_name,
        "institution": user.institution,
        "license_id": user.license_id,
        "is_active": user.is_active,
        "mfa_enabled": user.mfa_enabled,
        "role": user.role,
    }


@router.post("/forgot-password")
def forgot_password(payload: ForgotPasswordSchema, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == payload.email).first()
    if not user:
        # Don't reveal if email exists — return success anyway
        return {"msg": "If that email exists, a reset link has been sent"}
    token_data = {"sub": str(user.id)}
    token = auth.create_access_token(token_data, expires_delta=timedelta(hours=1))
    user.reset_token = token
    user.reset_token_expiry = datetime.utcnow() + timedelta(hours=1)
    db.commit()
    send_reset_email(payload.email, token)
    return {"msg": "If that email exists, a reset link has been sent"}


@router.post("/reset-password")
def reset_password(payload: ResetPasswordSchema, db: Session = Depends(get_db)):
    token_data = auth.decode_access_token(payload.token)
    if not token_data:
        raise HTTPException(status_code=400, detail="Invalid or expired token")
    user = db.query(models.User).filter(
        models.User.id == int(token_data["sub"])
    ).first()
    if not user or user.reset_token != payload.token:
        raise HTTPException(status_code=400, detail="Invalid or expired token")
    if user.reset_token_expiry and user.reset_token_expiry < datetime.utcnow():
        raise HTTPException(status_code=400, detail="Token expired")
    user.hashed_password = auth.get_password_hash(payload.new_password)
    user.reset_token = None
    user.reset_token_expiry = None
    db.commit()
    return {"msg": "Password reset successful"}
