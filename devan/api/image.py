import numpy as np
from typing import TypeAlias, Tuple
from pydantic import UUID4
from PIL import Image

from devan.api.model import ImageBody, ImageMode
from devan.api.utils import decode_image
from devan.constants.image import NORM_IMG_HEIGHT, NORM_IMG_WIDTH

_Mode: TypeAlias = str


def translate_image_mode(mode: ImageMode) -> _Mode | None:
    match mode:
        case "gray":
            return "L"
        case "rgb":
            return "RGB"
        case _:
            return None


def parse_image(payload: ImageBody) -> Tuple[UUID4, Image.Image]:
    # decode base64
    decoded = decode_image(payload.data)

    pixels = list(map(int, decoded.split(sep=",")))

    mode = translate_image_mode(payload.mode)

    img_arr = np.array(pixels, dtype=np.uint8)

    if img_arr.size != NORM_IMG_WIDTH * NORM_IMG_HEIGHT:
        raise RuntimeError(
            f"Client image is not normalized to {NORM_IMG_WIDTH}x{NORM_IMG_HEIGHT} pixels."
        )

    img_arr = img_arr.reshape(NORM_IMG_WIDTH, NORM_IMG_HEIGHT)

    return payload.id, Image.fromarray(img_arr, mode=mode)
