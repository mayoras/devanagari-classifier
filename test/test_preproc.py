import unittest
import numpy as np

from devan.preproc import (
    min_max_scaling,
    get_hog_desc,
    InvalidMinMaxValues,
    InvalidInputDimension,
)
from devan.constants.image import NORM_IMG_WIDTH, NORM_IMG_HEIGHT

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

    def test_get_hog_descriptor(self):
        NUM_CHARS = 3
        HOG_FD_SIZE = 128

        invalid_chars = get_random_chars(num_chars=NUM_CHARS, dim=5)
        plain_invalid = np.array([c.img_arr.flatten() for c in invalid_chars])

        # check if does not accept invalid dimensions
        self.assertRaises(InvalidInputDimension, lambda: get_hog_desc(plain_invalid))

        # WIDTH == HEIGHT for square character images
        valid_chars = get_random_chars(num_chars=NUM_CHARS, dim=NORM_IMG_WIDTH)
        plain_valid = np.array([c.img_arr.flatten() for c in valid_chars])

        # check return type for single and multiple chars
        ret_val_single = get_hog_desc(X=plain_valid[:1])
        ret_val_multiple = get_hog_desc(X=plain_valid)

        self.assertIsInstance(ret_val_single, np.ndarray)
        self.assertIsInstance(ret_val_multiple, np.ndarray)

        self.assertEqual(ret_val_single.shape, (1, HOG_FD_SIZE))
        self.assertEqual(ret_val_multiple.shape, (NUM_CHARS, HOG_FD_SIZE))
