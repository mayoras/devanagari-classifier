import re
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def contains_pattern(string: str, pattern: str) -> bool:
    return bool(re.search(pattern, string))


class Character:
    def __init__(
        self,
        filename: str | None = None,
        pil_img: Image.Image | None = None,
    ):
        if filename:
            print(f"using filename {filename} for instanciate the Character object")
            self.filename = filename
            self.img_arr = self._array_from_file(filename)
        elif pil_img:
            self.filename = None
            self.img_arr = self._array_from_pil(pil_img)
        else:
            raise NotImplementedError(
                "not instanciating Character nor from file nor from PIL.Image"
            )

    def _array_from_file(self, filename: str) -> np.ndarray:
        pil_img = Image.open(filename, "r")
        return self._array_from_pil(pil_img)

    def _array_from_pil(self, pil_img: Image.Image) -> np.ndarray:
        return np.array(pil_img, dtype=np.uint8)

    def show_character(self):
        plt.imshow(self.img_arr, cmap="gray")
        plt.axis("off")
        plt.title("Character image")

        plt.show()

    def save_character_image(self, filename: str):
        pil_img = Image.fromarray(self.img_arr)

        fmt = (
            None
            if contains_pattern(filename, r"/\.(gif|jpe?g|tiff?|png|webp|bmp)$/i")
            else "png"
        )

        if not fmt:
            print("using PNG format to save the character image.")

        pil_img.save(filename, format=fmt, bitmap_format="bmp")
