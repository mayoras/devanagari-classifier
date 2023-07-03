import matplotlib.pyplot as plt
from skimage.feature import hog

BYTE_SIZE = 255

# TODO: make compatible with a group of characters


def min_max_scaling(arr):
    return arr / BYTE_SIZE


def get_hog_desc(X):
    # reconvert feature vector in a matrix (image)
    X_aux = X.reshape(32, 32)

    # return the HOG descriptor of the image
    fd, image = hog(
        X_aux,
        orientations=8,
        pixels_per_cell=(8, 8),
        cells_per_block=(1, 1),
        block_norm="L2-Hys",
        visualize=True,
    )

    plt.imshow(image, cmap="gray")
    plt.show()

    return fd


def transform_input(arr):
    # get row vector of initial features
    X = arr.reshape(1, -1).flatten()

    # do MinMax-scaling to normalize to [0,1]
    X = min_max_scaling(X)

    # extract features
    X = get_hog_desc(X)

    return X
