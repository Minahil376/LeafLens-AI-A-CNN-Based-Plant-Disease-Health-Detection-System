"""Image preprocessing module for the plant disease detection backend."""

import io

import numpy as np
from PIL import Image


def preprocess_image(image_bytes: bytes) -> np.ndarray:
    """Decode, resize, and prepare image bytes for model inference.

    Args:
        image_bytes: Raw bytes of a JPEG, PNG, or WebP image.

    Returns:
        A numpy array of shape (1, 224, 224, 3), dtype float32, with pixel
        values normalized to [0, 1].  The model's built-in Rescaling layer
        (scale=255.0) multiplies these back to [0, 255] as ResNet50 expects.

    Raises:
        ValueError: If the bytes cannot be decoded as a valid image.
    """
    try:
        image = Image.open(io.BytesIO(image_bytes))
        image = image.convert("RGB")
    except Exception as exc:
        raise ValueError(
            "Could not decode the uploaded file as an image."
        ) from exc

    image = image.resize((224, 224), Image.LANCZOS)
    arr = np.array(image, dtype=np.float32) / 255.0  # normalize to [0, 1] — model's Rescaling(scale=255) multiplies back to [0, 255]
    arr = np.expand_dims(arr, axis=0)      # shape (1, 224, 224, 3)
    return arr
