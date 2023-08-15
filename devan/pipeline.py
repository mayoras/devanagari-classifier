from typing import Callable, TypeAlias, List
import numpy as np

from sklearn.neural_network import MLPClassifier

from devan.character import Character

Transform: TypeAlias = tuple[Callable, dict]
TransformList: TypeAlias = list[Transform]


class TestInputNotDefined(Exception):
    def __init__(self):
        super().__init__("Test input for prediction is not defined.")


class PipelineModelNotDefined(Exception):
    def __init__(self):
        super().__init__("Model not defined in pipeline.")


class PipelineInputNotDefined(Exception):
    def __init__(self):
        super().__init__("Pipeline input not defined or empty.")


class Pipeline:
    # transformation === (func, {param1: p1, param2: p2})
    def __init__(
        self,
        chars: list[Character],
        trans: TransformList = [],
        model: MLPClassifier | None = None,
    ):
        # init prediction set and transformations
        self.X: np.ndarray[int, np.dtype[np.float64]] = np.array(
            [c.img_arr for c in chars], dtype=np.float64
        )
        self.trans = trans
        self.model = model
        self.X_test = None

    def add_transform(self, trans: Transform):
        self.trans.append(trans)

    def add_multi_transform(self, trans: TransformList):
        self.trans.extend(trans)

    def transform(self):
        if self.X.size == 0:
            raise PipelineInputNotDefined

        # reshape the images to 1D-array of pixels
        X_aux = self.X.reshape(self.X.shape[0], -1)

        # Apply transformations to all images
        for fun, params in self.trans:
            X_aux = fun(X_aux, **params)

        self.X_test = X_aux.copy()
        return X_aux

    def predict(self) -> List[int]:
        if self.X_test is None:
            raise TestInputNotDefined
        if self.model is None:
            raise PipelineModelNotDefined

        pred = self.model.predict(self.X_test).tolist()

        return pred
