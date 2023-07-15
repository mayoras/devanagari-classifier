import os

from joblib import load

from sklearn.neural_network import MLPClassifier


class ModelObjectNotFound(Exception):
    def __init__(self, filename) -> None:
        self.message = f"Model object {filename} not found"


def load_model(filename: str) -> MLPClassifier:
    if not os.path.exists(filename):
        raise ModelObjectNotFound(filename)

    return load(filename)
