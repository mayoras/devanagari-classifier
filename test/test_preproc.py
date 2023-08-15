import unittest
import numpy as np

from devan.preproc import min_max_scaling, InvalidMinMaxValues

from test.mocks.character import get_random_chars


class TestPreproc(unittest.TestCase):
    def test_min_max_scaling(self):
        # 5x5 chars
        chars = get_random_chars(num_chars=3, dim=5)

        plain_chars = np.array([c.img_arr.flatten() for c in chars])

        # check if all values are normalized for single char
        norm_single_char = min_max_scaling(X=plain_chars[:1])
        self.assertTrue(
            all(x >= 0 and x <= 1 for x in norm_single_char.flatten().tolist())
        )

        # check if all values are normalized for multiple chars
        norm_multiple_chars = min_max_scaling(X=plain_chars)
        self.assertTrue(
            all(x >= 0 and x <= 1 for x in norm_multiple_chars.flatten().tolist())
        )

        # check invalid min max values
        min_max_equal = lambda: min_max_scaling(
            X=plain_chars,
            min_vals=np.repeat(0, plain_chars.shape[1]),
            max_vals=np.repeat(0, plain_chars.shape[1]),
        )
        self.assertRaises(InvalidMinMaxValues, min_max_equal)

        min_max_negative = lambda: min_max_scaling(
            X=plain_chars,
            min_vals=np.repeat(1, plain_chars.shape[1]),
            max_vals=np.repeat(0, plain_chars.shape[1]),
        )
        self.assertRaises(InvalidMinMaxValues, min_max_negative)
