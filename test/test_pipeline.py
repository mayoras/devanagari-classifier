import unittest
import numpy as np

from devan.pipeline import Pipeline
from test.mocks.character import get_blank_char_mock


def fill_main_diagonal(arr: np.ndarray, val: int) -> np.ndarray:
    # for each char array
    for i, c in enumerate(arr):
        # convert c in matrix
        n = int(np.sqrt(c.size))
        mat = c.reshape((n, n))

        # fill diagonal
        np.fill_diagonal(mat, val)
        arr[i] = mat.flatten()

    return arr


def fill_anti_diagonal(arr: np.ndarray, val: int) -> np.ndarray:
    # for each char array
    for i, c in enumerate(arr):
        # convert c in matrix
        n = int(np.sqrt(c.size))
        mat = c.reshape((n, n))

        # fill diagonal
        np.fill_diagonal(np.fliplr(mat), val)
        arr[i] = mat.flatten()

    return arr


class TestPipeline(unittest.TestCase):
    def test_single_char_transform(self):
        # simple blank 5x5 character
        N = 5
        mock_char = get_blank_char_mock(n=N)

        pipeline = Pipeline(chars=[mock_char])

        # add transforms
        pipeline.add_multi_transform(
            [
                (fill_main_diagonal, {"val": 1}),
                (fill_anti_diagonal, {"val": 2}),
            ]
        )

        # apply transforms
        transformed_chars = pipeline.transform()
        char_trans = transformed_chars[0].reshape(N, N)

        # check main diagonal
        self.assertListEqual(np.diag(char_trans).tolist(), [1, 1, 2, 1, 1])

        # check anti diagonal
        self.assertListEqual(np.diag(np.fliplr(char_trans)).tolist(), [2] * N)

    def test_transform_order(self):
        # simple blank 5x5 character
        N = 5
        mock_char = get_blank_char_mock(n=N)

        pipeline = Pipeline(chars=[mock_char])

        # add transforms
        pipeline.add_multi_transform(
            [
                (fill_main_diagonal, {"val": 1}),
                (fill_main_diagonal, {"val": 2}),
            ]
        )

        # apply transforms
        transformed_chars = pipeline.transform()
        char_trans = transformed_chars[0].reshape(N, N)

        # check the second transform was the last applied
        self.assertListEqual(np.diag(char_trans).tolist(), [2] * N)
