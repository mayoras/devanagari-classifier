import numpy as np

from typing import Callable, TypeAlias
from devan.character import Character

Transform: TypeAlias = tuple[Callable, dict]
TransformList: TypeAlias = list[Transform]


class Pipeline:
    # transformation === (func, {param1: p1, param2: p2})
    def __init__(self, chars: list[Character], trans: TransformList = []):
        # init prediction set and transformations
        self.X: np.ndarray[int, np.dtype[np.float64]] = np.array(
            [c.img_arr for c in chars], dtype=np.float64
        )
        self.trans = trans

    def add_transform(self, trans: Transform):
        self.trans.append(trans)

    def add_multi_transform(self, trans: TransformList):
        self.trans.extend(trans)

    def transform(self):
        # reshape the images to 1D-array of pixels
        X_aux = self.X.reshape(self.X.shape[0], -1)

        # Apply transformations
        for fun, params in self.trans:
            X_aux = fun(**params)

        return X_aux
