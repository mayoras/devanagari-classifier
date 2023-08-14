import numpy as np

from PIL import Image

from devan.character import Character


def get_blank_char_mock(n: int) -> Character:
    zero_img = Image.fromarray(np.zeros(shape=(n, n)))
    blank = Character(pil_img=zero_img)

    return blank
