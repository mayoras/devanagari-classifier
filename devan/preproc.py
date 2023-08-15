import numpy as np
from skimage.feature import hog

BYTE_SIZE = 255


class InvalidInputDimension(Exception):
    def __init__(self) -> None:
        self.message = f"Input dimension should be {32 * 32}"


class InvalidMinMaxValues(Exception):
    def __init__(self, msg) -> None:
        self.message = msg


def byte_normalize(arr):
    return arr / BYTE_SIZE


def min_max_scaling(X, min_vals=None, max_vals=None):
    if X.shape[0] == 1 or min_vals is None or max_vals is None:
        print("Warning: using byte-normalization")
        return byte_normalize(X)

    if np.any((max_vals - min_vals) <= 0):
        raise InvalidMinMaxValues(
            "column max values have to be greater than min values."
        )

    norm = np.zeros(X.shape, dtype=float)

    zero_cols = np.where(np.all(X == 0, axis=0))[0]

    # for each column
    for i in range(X.shape[1]):
        if i in zero_cols:
            norm[:, i] = X[:, i]
        else:
            norm[:, i] = (X[:, i] - min_vals[i]) / (max_vals[i] - min_vals[i])

    return norm


def get_hog_desc(X):
    # is a single image
    if X.shape[0] == 1:
        if X.shape[1] != 32 * 32:
            raise InvalidInputDimension

        # reconvert feature vector in a matrix (image)
        X_aux = X.reshape(32, 32)

        # return the HOG descriptor of the image
        return hog(
            X_aux,
            orientations=8,
            pixels_per_cell=(8, 8),
            cells_per_block=(1, 1),
            block_norm="L2-Hys",
        )
    else:
        if X.shape[1] != 32 * 32:
            raise InvalidInputDimension

        X_aux = X.reshape(X.shape[0], 32, 32)
        # por cada ejemplo, obtenemos su respectivo descriptor HOG
        fds = []
        for e in X_aux:
            fd = hog(
                e,
                orientations=8,
                pixels_per_cell=(8, 8),
                cells_per_block=(1, 1),
                block_norm="L2-Hys",
            )
            fds.append(fd)

        # devolver el nuevo conjunto de train
        return np.array(fds)


def transform_input(arr):
    # get row vector of initial features
    X = arr.reshape(1, -1).flatten()

    # do MinMax-scaling to normalize to [0,1]
    X = min_max_scaling(X)

    # extract features
    X = get_hog_desc(X)

    return X
