import numpy as np

from PIL import Image

from devan.character import Character


def get_blank_char_mock(n: int) -> Character:
    zero_img = Image.fromarray(np.zeros(shape=(n, n)))
    blank = Character(pil_img=zero_img)

    return blank


def get_random_chars(num_chars: int, dim: int) -> list[Character]:
    chars_arr = np.array(
        [
            np.random.randint(0, 255, (dim, dim), dtype=np.uint8)
            for _ in range(num_chars)
        ]
    )

    return [Character(pil_img=Image.fromarray(arr)) for arr in chars_arr]
