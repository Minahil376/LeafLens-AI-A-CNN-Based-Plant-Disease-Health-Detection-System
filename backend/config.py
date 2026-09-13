import os
from dataclasses import dataclass


@dataclass
class Settings:
    MODEL_DIR: str = os.getenv("MODEL_DIR", ".")
    CORS_ORIGINS: str = os.getenv("CORS_ORIGINS", "*")
    MAX_UPLOAD_BYTES: int = int(os.getenv("MAX_UPLOAD_BYTES", "10485760"))
    INFERENCE_TIMEOUT_SECONDS: int = int(os.getenv("INFERENCE_TIMEOUT_SECONDS", "30"))


settings = Settings()
