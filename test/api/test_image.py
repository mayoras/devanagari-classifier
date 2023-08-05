import unittest
import api.image as img

from api.model import ImageBody

DATA_FILENAME = "./test/api/data.txt"

fake_payload = {
    "file": "image",
    "mode": "gray",
    "alpha": False,
}

with open(DATA_FILENAME, "r") as file:
    fake_payload["data"] = file.read()

fake_image_body = ImageBody(**fake_payload)

IMG_WIDTH = 32
IMG_HEIGHT = 32


class TestImage(unittest.TestCase):
    def test_parse_img(self):
        pil_img = img.parse_image(payload=fake_image_body)

        pil_img.show()

        self.assertIsNotNone(pil_img, msg="PILLOW Image should not be None")
        self.assertEquals(
            pil_img.width, IMG_WIDTH, msg=f"Image should have width {IMG_WIDTH}"
        )
        self.assertEquals(
            pil_img.height, IMG_HEIGHT, msg=f"Image should have height {IMG_HEIGHT}"
        )
        self.assertEquals(
            pil_img.mode, "L", msg=f"Image mode should be grayscale (8-bit pixels)"
        )
