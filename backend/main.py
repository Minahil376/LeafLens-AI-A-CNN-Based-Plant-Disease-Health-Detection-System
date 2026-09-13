"""FastAPI application entry point for the plant disease detection web app."""

import asyncio
import logging
import traceback
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles

from backend.classifier import classifier
from backend.config import settings
from backend.inference import engine
from backend.schemas import HealthResponse, PredictionResult

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Allowed MIME types
# ---------------------------------------------------------------------------
ALLOWED_MIME_TYPES = {"image/jpeg", "image/png", "image/webp"}


# ---------------------------------------------------------------------------
# Lifespan — load model once at startup
# ---------------------------------------------------------------------------

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Load the inference model at startup; nothing to clean up on shutdown."""
    engine.load(settings.MODEL_DIR)
    yield


# ---------------------------------------------------------------------------
# App factory
# ---------------------------------------------------------------------------

app = FastAPI(
    title="Plant Disease Detection",
    description="AI-powered plant disease diagnosis from leaf images.",
    version="1.0.0",
    lifespan=lifespan,
)

# CORS
origins = [o.strip() for o in settings.CORS_ORIGINS.split(",") if o.strip()]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins if origins != ["*"] else ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------

@app.get("/health", response_model=HealthResponse)
async def health() -> JSONResponse:
    """Return server readiness status."""
    if engine.is_loaded:
        return JSONResponse(
            status_code=200,
            content={"status": "ok", "model_loaded": True},
        )
    return JSONResponse(
        status_code=503,
        content={"status": "error", "model_loaded": False},
    )


@app.post("/predict", response_model=PredictionResult)
async def predict(file: UploadFile) -> PredictionResult:
    """Accept an image upload and return a plant disease prediction.

    Validates MIME type and file size before running inference.
    """
    # ---- MIME type validation ----
    content_type = file.content_type or ""
    if content_type not in ALLOWED_MIME_TYPES:
        raise HTTPException(
            status_code=422,
            detail="Unsupported file type. Accepted: JPEG, PNG, WebP.",
        )

    # ---- Read file bytes ----
    image_bytes = await file.read()

    # ---- Size validation ----
    if len(image_bytes) > settings.MAX_UPLOAD_BYTES:
        raise HTTPException(
            status_code=422,
            detail=f"File exceeds {settings.MAX_UPLOAD_BYTES // (1024 * 1024)} MB limit.",
        )

    # ---- Check model is available ----
    if not engine.is_loaded:
        raise HTTPException(status_code=503, detail="Model is not available.")

    # ---- Inference (with timeout) ----
    loop = asyncio.get_event_loop()
    try:
        probabilities = await asyncio.wait_for(
            loop.run_in_executor(None, engine.predict, image_bytes),
            timeout=settings.INFERENCE_TIMEOUT_SECONDS,
        )
    except asyncio.TimeoutError:
        raise HTTPException(status_code=504, detail="Inference timed out.")
    except ValueError as exc:
        # Image could not be decoded
        raise HTTPException(status_code=422, detail=str(exc))
    except Exception:
        logger.error("Unexpected inference error:\n%s", traceback.format_exc())
        raise HTTPException(status_code=500, detail="An internal error occurred.")

    # ---- Classify ----
    result = classifier.classify(probabilities)
    logger.info(
        "Prediction: %s (%.1f%%) | top-3: %s",
        result.class_label,
        result.confidence * 100,
        [(item.class_label, f"{item.confidence*100:.1f}%") for item in result.top_k],
    )
    return result


# ---------------------------------------------------------------------------
# Static files — serve the React production build
# ---------------------------------------------------------------------------

_dist_dir = Path(__file__).parent.parent / "frontend" / "dist"
_frontend_dir = Path(__file__).parent.parent / "frontend"

# Prefer the React build (dist/) if it exists, otherwise fall back to raw frontend/
_serve_dir = _dist_dir if _dist_dir.is_dir() else _frontend_dir

if _serve_dir.is_dir():
    from fastapi.responses import HTMLResponse, FileResponse  # noqa: F401

    class NoCacheStaticFiles(StaticFiles):
        """StaticFiles that adds no-cache headers to every response."""
        async def get_response(self, path: str, scope):
            response = await super().get_response(path, scope)
            response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
            response.headers["Pragma"] = "no-cache"
            response.headers["Expires"] = "0"
            return response

    # Serve static assets (/assets/*, /logo.png, etc.)
    app.mount("/", NoCacheStaticFiles(directory=str(_serve_dir), html=True), name="frontend")
