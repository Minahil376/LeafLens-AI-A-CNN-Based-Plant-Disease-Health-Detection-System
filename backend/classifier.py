"""Classifier module: maps raw softmax probabilities to PredictionResult."""

import numpy as np

from backend.disease_info import DISEASE_INFO
from backend.schemas import PredictionResult, TopKItem


class Classifier:
    """Maps a 38-element probability vector to a structured PredictionResult."""

    def classify(self, probabilities: np.ndarray, k: int = 3) -> PredictionResult:
        """Select the top-k predictions and look up disease information.

        Args:
            probabilities: A 1-D numpy array of shape (38,) containing
                softmax probabilities.
            k: Number of top predictions to include in *top_k*.

        Returns:
            A :class:`PredictionResult` containing the primary prediction and
            the top-k list ordered from highest to lowest confidence.
        """
        # Descending sort by probability
        sorted_indices = np.argsort(probabilities)[::-1]
        top_indices = sorted_indices[:k]

        top_k_items = []
        for idx in top_indices:
            class_index = int(idx)
            confidence = round(float(probabilities[idx]), 4)
            if class_index in DISEASE_INFO:
                label = DISEASE_INFO[class_index].class_label
            else:
                label = _fallback_label(class_index)
            top_k_items.append(TopKItem(class_label=label, confidence=confidence))

        # Primary prediction is the top-1
        primary_index = int(top_indices[0])
        primary_confidence = round(float(probabilities[top_indices[0]]), 4)

        if primary_index in DISEASE_INFO:
            entry = DISEASE_INFO[primary_index]
            return PredictionResult(
                class_label=entry.class_label,
                confidence=primary_confidence,
                is_healthy=entry.is_healthy,
                plant_name=entry.plant_name,
                disease_name=entry.disease_name,
                description=entry.description,
                treatment=entry.treatment,
                top_k=top_k_items,
            )

        # Fallback for unknown index (satisfies Requirement 8.3)
        raw_label = _fallback_label(primary_index)
        return PredictionResult(
            class_label=raw_label,
            confidence=primary_confidence,
            is_healthy=False,
            plant_name="Unknown",
            disease_name="Unknown",
            description=(
                f"Detailed information is unavailable for class index {primary_index}. "
                "Please consult a plant pathologist for diagnosis."
            ),
            treatment=["Consult a plant pathologist for diagnosis and treatment recommendations."],
            top_k=top_k_items,
        )


def _fallback_label(class_index: int) -> str:
    """Derive a human-readable label from the raw class index."""
    return f"Class {class_index} (no details available)"


# Module-level singleton used by main.py
classifier = Classifier()
