from joblib import load
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


class Character:
    def __init__(self, filename: str):
        self.filename = filename
        self.img_arr = self._read_image(filename)

    def _read_image(self, filename: str) -> np.ndarray(shape=(32, 32), dtype=np.int32):
        pil_img = Image.open(filename, "r")
        return np.array(pil_img, dtype=np.int32)

    def show_character(self):
        plt.imshow(self.img_arr, cmap="gray")
        plt.axis("off")
        plt.title("Character image")

        plt.show()