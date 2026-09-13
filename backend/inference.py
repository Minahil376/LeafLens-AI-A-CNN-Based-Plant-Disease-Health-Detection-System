"""Inference engine that loads and runs the Keras plant disease model."""

import logging
import os
import sys

import numpy as np

from backend.preprocessing import preprocess_image

logger = logging.getLogger(__name__)


class InferenceEngine:
    """Wraps a Keras model for plant disease inference.

    Usage::

        engine = InferenceEngine()
        engine.load("/path/to/model_dir")
        probabilities = engine.predict(image_bytes)
    """

    def __init__(self) -> None:
        self._model = None

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def load(self, model_dir: str) -> None:
        """Load the Keras model from *model_dir*.

        Expects ``config.json`` and ``model.weights.h5`` in *model_dir*.
        Logs a FATAL message and exits with code 1 if either file is missing.
        """
        config_path = os.path.join(model_dir, "config.json")
        weights_path = os.path.join(model_dir, "model.weights.h5")

        if not os.path.isfile(config_path) or not os.path.isfile(weights_path):
            logger.critical(
                "FATAL: Model files not found in %s. Exiting.", model_dir
            )
            sys.exit(1)

        try:
            import keras  # noqa: PLC0415 – lazy import to keep startup fast

            with open(config_path, "r", encoding="utf-8") as fh:
                config_json = fh.read()

            model = keras.models.model_from_json(config_json)
            model.load_weights(weights_path)
            self._model = model
            logger.info("Model loaded successfully from %s", model_dir)
        except Exception:
            logger.critical(
                "FATAL: Failed to load model from %s. Exiting.", model_dir,
                exc_info=True,
            )
            sys.exit(1)

    def predict(self, image_bytes: bytes) -> np.ndarray:
        """Run inference on raw image bytes.

        Args:
            image_bytes: Raw image bytes (JPEG, PNG, or WebP).

        Returns:
            A 1-D numpy array of shape (38,) containing the softmax
            probabilities for each of the 38 PlantVillage classes.

        Raises:
            ValueError: If *image_bytes* cannot be decoded as an image.
            RuntimeError: If the model has not been loaded yet.
        """
        if self._model is None:
            raise RuntimeError("Model is not loaded. Call load() first.")

        batch = preprocess_image(image_bytes)  # (1, 224, 224, 3)
        predictions = self._model.predict(batch, verbose=0)  # (1, 38)
        return predictions[0]  # (38,)

    @property
    def is_loaded(self) -> bool:
        """Return True if the model has been loaded successfully."""
        return self._model is not None


# Module-level singleton used by main.py
engine = InferenceEngine()
