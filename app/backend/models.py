from sqlalchemy import Column, Integer, String, Boolean, DateTime, Float, Text, ForeignKey
from datetime import datetime
from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String, nullable=True)
    institution = Column(String, nullable=True)
    license_id = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    totp_secret = Column(String, nullable=True)
    mfa_enabled = Column(Boolean, default=False)
    role = Column(String, default="doctor")
    reset_token = Column(String, nullable=True)
    reset_token_expiry = Column(DateTime, nullable=True)


class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    patient_uid = Column(String, unique=True, index=True)   # e.g. PID-0001
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=True)
    gender = Column(String, nullable=True)
    tissue_type = Column(String, nullable=True)             # Breast, Colon, etc.
    notes = Column(Text, nullable=True)
    risk_score = Column(Float, nullable=True)               # 0–100 from AI
    risk_label = Column(String, nullable=True)              # Benign / Malignant / Inflammatory
    status = Column(String, default="Pending")              # Pending / Analyzed / Reviewed
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    doctor_id = Column(Integer, ForeignKey("users.id"), nullable=True)
