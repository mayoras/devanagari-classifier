import numpy as np

from typing import Callable
from devan.character import Character


class Pipeline:
    # transformation === (func, {param1: p1, param2: p2})
    def __init__(self, chars: list[Character], trans: list[tuple[Callable, dict]] = []):
        # init prediction set and transformations
        self.X: np.ndarray[int, np.dtype[np.float64]] = np.array(
            [c.img_arr for c in chars], dtype=np.float64
        )
        self.trans = trans

    def add_transform(self, trans: tuple[Callable, dict]):
        self.trans.append(trans)

    def transform(self):
        # reshape the images to 1D-array of pixels
        X_aux = self.X.reshape(self.X.shape[0], -1)

        # Apply transformations
        for fun, params in self.trans:
            X_aux = fun(**params)

        return X_aux
