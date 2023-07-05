import numpy as np
from devan.character import Character

# TODO: refine transformations to be more parameterizable


class Pipeline:
    def __init__(self, chars: list[Character]):
        self.X = np.array([c.img_arr for c in chars], dtype=float)
        self.trans = []

    def __init__(self, chars: list[Character], trans: list[callable]):
        self.X = np.array([c.img_arr for c in chars], dtype=float)
        self.trans = trans

    def transform(self):
        # reshape the images to 1D-array of pixels
        X_aux = self.X.reshape(self.X.shape[0], -1)

        # Apply transformations
        for t in self.trans:
            X_aux = t(X_aux)

        return X_aux
