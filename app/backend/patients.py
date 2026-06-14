from fastapi import APIRouter, Depends, HTTPException, status, Request
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
import random
import string

from .database import get_db
from . import models
from .auth import decode_access_token

router = APIRouter(prefix="/patients", tags=["patients"])


# ── Auth helper ────────────────────────────────────────────────────────────────
def get_current_user(request: Request, db: Session = Depends(get_db)):
    token = request.cookies.get("access_token") or (
        request.headers.get("Authorization", "").replace("Bearer ", "").strip() or None
    )
    if not token:
        raise HTTPException(status_code=401, detail="Not authenticated")
    payload = decode_access_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    user = db.query(models.User).filter(models.User.id == int(payload["sub"])).first()
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    return user


# ── Schemas ────────────────────────────────────────────────────────────────────
class PatientCreate(BaseModel):
    name: str
    age: Optional[int] = None
    gender: Optional[str] = None
    tissue_type: Optional[str] = None
    notes: Optional[str] = None


class PatientUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    gender: Optional[str] = None
    tissue_type: Optional[str] = None
    notes: Optional[str] = None
    risk_score: Optional[float] = None
    risk_label: Optional[str] = None
    status: Optional[str] = None


def _uid():
    chars = string.digits
    return "PID-" + "".join(random.choices(chars, k=6))


def _patient_dict(p: models.Patient) -> dict:
    return {
        "id": p.id,
        "patient_uid": p.patient_uid,
        "name": p.name,
        "age": p.age,
        "gender": p.gender,
        "tissue_type": p.tissue_type,
        "notes": p.notes,
        "risk_score": p.risk_score,
        "risk_label": p.risk_label,
        "status": p.status,
        "created_at": p.created_at.isoformat() if p.created_at else None,
        "updated_at": p.updated_at.isoformat() if p.updated_at else None,
    }


# ── Routes ─────────────────────────────────────────────────────────────────────
@router.get("/")
def list_patients(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
    q: Optional[str] = None,
):
    query = db.query(models.Patient).filter(models.Patient.doctor_id == current_user.id)
    if q:
        query = query.filter(
            models.Patient.name.ilike(f"%{q}%") | models.Patient.patient_uid.ilike(f"%{q}%")
        )
    patients = query.order_by(models.Patient.created_at.desc()).all()
    return [_patient_dict(p) for p in patients]


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_patient(
    data: PatientCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    uid = _uid()
    # ensure uniqueness
    while db.query(models.Patient).filter(models.Patient.patient_uid == uid).first():
        uid = _uid()

    patient = models.Patient(
        patient_uid=uid,
        name=data.name,
        age=data.age,
        gender=data.gender,
        tissue_type=data.tissue_type,
        notes=data.notes,
        status="Pending",
        doctor_id=current_user.id,
    )
    db.add(patient)
    db.commit()
    db.refresh(patient)
    return _patient_dict(patient)


@router.get("/{patient_id}")
def get_patient(
    patient_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    p = db.query(models.Patient).filter(
        models.Patient.id == patient_id, models.Patient.doctor_id == current_user.id
    ).first()
    if not p:
        raise HTTPException(status_code=404, detail="Patient not found")
    return _patient_dict(p)


@router.put("/{patient_id}")
def update_patient(
    patient_id: int,
    data: PatientUpdate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    p = db.query(models.Patient).filter(
        models.Patient.id == patient_id, models.Patient.doctor_id == current_user.id
    ).first()
    if not p:
        raise HTTPException(status_code=404, detail="Patient not found")
    for field, value in data.dict(exclude_unset=True).items():
        setattr(p, field, value)
    p.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(p)
    return _patient_dict(p)


@router.delete("/{patient_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_patient(
    patient_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    p = db.query(models.Patient).filter(
        models.Patient.id == patient_id, models.Patient.doctor_id == current_user.id
    ).first()
    if not p:
        raise HTTPException(status_code=404, detail="Patient not found")
    db.delete(p)
    db.commit()
    return None
