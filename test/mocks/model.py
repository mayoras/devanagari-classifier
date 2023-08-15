import numpy as np
from typing import List

from sklearn.neural_network import MLPClassifier


class MockMLPClassifier(MLPClassifier):
    """
    Mock expected behaviour of a classifier model.
    """

    def __init__(self, labels: List[int], **kargs):
        self.labels = labels
        super().__init__(**kargs)

    def predict(self, _X_test) -> np.ndarray:
        # should return the expected label.
        return np.array(self.labels, dtype=int)
