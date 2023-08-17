import unittest
import devan.api.image as img

from devan.constants.image import NORM_IMG_HEIGHT, NORM_IMG_WIDTH
from test.mocks.api.image import get_mock_image_body


class TestImage(unittest.TestCase):
    def test_parse_img(self):
        fake_image_body = get_mock_image_body()

        _id, pil_img = img.parse_image(payload=fake_image_body)

        # pil_img.show()

        self.assertIsNotNone(pil_img, msg="PILLOW Image should not be None")
        self.assertEqual(
            pil_img.width,
            NORM_IMG_WIDTH,
            msg=f"Image should have width {NORM_IMG_WIDTH}",
        )
        self.assertEqual(
            pil_img.height,
            NORM_IMG_HEIGHT,
            msg=f"Image should have height {NORM_IMG_HEIGHT}",
        )
        self.assertEqual(
            pil_img.mode, "L", msg=f"Image mode should be grayscale (8-bit pixels)"
        )
