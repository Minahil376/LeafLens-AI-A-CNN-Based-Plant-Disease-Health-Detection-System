from pydantic import BaseModel


class TopKItem(BaseModel):
    class_label: str
    confidence: float


class PredictionResult(BaseModel):
    class_label: str
    confidence: float
    is_healthy: bool
    plant_name: str
    disease_name: str
    description: str
    treatment: list[str]
    top_k: list[TopKItem]


class HealthResponse(BaseModel):
    status: str
    model_loaded: bool
