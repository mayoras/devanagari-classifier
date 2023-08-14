import os
from constants.character import LABELS_TRANS

from joblib import load

from sklearn.neural_network import MLPClassifier


class ModelObjectNotFound(Exception):
    def __init__(self, filename) -> None:
        self.message = f"Model object {filename} not found"


class LabelError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


def load_model(filename: str) -> MLPClassifier:
    if not os.path.exists(filename):
        raise ModelObjectNotFound(filename)

    return load(filename)


def label_to_char_name(label: int) -> str:
    if label not in range(0, len(LABELS_TRANS)):
        raise LabelError(message=f"{label} is an invalid label.")

    return LABELS_TRANS[label].split("_")[-1]
