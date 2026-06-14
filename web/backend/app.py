import os
from contextlib import asynccontextmanager

from fastapi import FastAPI, UploadFile, File, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from .database import init_db
from .auth_routes import router as auth_router
from .patients import router as patients_router

# ── Startup / shutdown ─────────────────────────────────────────────────────────
@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()   # create tables if they don't exist
    yield

app = FastAPI(title="PathoAI Clinical Suite", lifespan=lifespan)

# ── CORS ───────────────────────────────────────────────────────────────────────
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── API Routers ────────────────────────────────────────────────────────────────
app.include_router(auth_router)
app.include_router(patients_router)

# ── Health check ───────────────────────────────────────────────────────────────
@app.get("/health")
async def health():
    return {"status": "ok", "service": "PathoAI Clinical Suite"}


# ── AI Prediction (optional — graceful fallback if torch not installed) ────────
try:
    import io
    import numpy as np
    import torch
    from PIL import Image
    from dotenv import load_dotenv

    load_dotenv()

    MODEL_PATH = os.getenv("PATHOAI_MODEL", "models/model.pth")

    class SimpleCNN(torch.nn.Module):
        def __init__(self, num_classes=3):
            super().__init__()
            self.features = torch.nn.Sequential(
                torch.nn.Conv2d(3, 16, kernel_size=3, stride=2, padding=1),
                torch.nn.ReLU(inplace=True),
                torch.nn.AdaptiveAvgPool2d((1, 1)),
            )
            self.classifier = torch.nn.Linear(16, num_classes)

        def forward(self, x):
            x = self.features(x)
            x = torch.flatten(x, 1)
            return self.classifier(x)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    _model = SimpleCNN(num_classes=3)
    if os.path.exists(MODEL_PATH):
        _model.load_state_dict(torch.load(MODEL_PATH, map_location=device))
    _model.eval().to(device)

    DISEASE_MAP = {
        0: {"label": "Benign Tissue", "description": "No pathological findings detected.", "risk": 10},
        1: {"label": "Malignant Tumor", "description": "Features consistent with malignancy.", "risk": 88},
        2: {"label": "Inflammatory Lesion", "description": "Signs of active inflammation present.", "risk": 42},
    }

    def _preprocess(image_bytes: bytes) -> torch.Tensor:
        img = Image.open(io.BytesIO(image_bytes)).convert("RGB")
        img = img.resize((224, 224))
        arr = np.array(img).astype(np.float32) / 255.0
        arr = np.transpose(arr, (2, 0, 1))
        return torch.from_numpy(arr).unsqueeze(0).to(device)

    @app.post("/predict")
    async def predict(file: UploadFile = File(...)):
        if file.content_type not in ["image/jpeg", "image/png", "image/jpg"]:
            raise HTTPException(status_code=400, detail="Unsupported file type")
        content = await file.read()
        try:
            tensor = _preprocess(content)
            with torch.no_grad():
                logits = _model(tensor)
                probs = torch.nn.functional.softmax(logits, dim=1).cpu().numpy()[0]
            idx = int(probs.argmax())
            disease = DISEASE_MAP.get(idx, {"label": "Unknown", "description": "", "risk": 0})
            return JSONResponse({
                "label": disease["label"],
                "confidence": round(float(probs[idx]), 4),
                "description": disease["description"],
                "risk_score": disease["risk"],
            })
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    print("[OK] AI prediction engine loaded (torch available)")

except ImportError:
    @app.post("/predict")
    async def predict_stub(file: UploadFile = File(...)):
        """Stub when torch is not installed — returns a simulated result."""
        import random
        labels = [
            {"label": "Benign Tissue", "description": "No pathological findings detected.", "risk_score": random.randint(5, 20)},
            {"label": "Malignant Tumor", "description": "Features consistent with malignancy.", "risk_score": random.randint(70, 95)},
            {"label": "Inflammatory Lesion", "description": "Signs of active inflammation present.", "risk_score": random.randint(30, 55)},
        ]
        result = random.choice(labels)
        result["confidence"] = round(random.uniform(0.82, 0.98), 4)
        return JSONResponse(result)

    print("[WARN] torch not found — using simulated AI predictions")


# ── Serve Frontend SPA ─────────────────────────────────────────────────────────
_FRONTEND_DIR = os.path.join(os.path.dirname(__file__), "..", "frontend")
if os.path.isdir(_FRONTEND_DIR):
    app.mount("/", StaticFiles(directory=_FRONTEND_DIR, html=True), name="frontend")


# ── Entry point ────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.app:app", host="127.0.0.1", port=8000, reload=True)
