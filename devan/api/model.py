from typing import Literal
from pydantic import BaseModel


ImageMode = Literal["gray", "rgb"]


class ImageBody(BaseModel):
    file: str
    mode: ImageMode = "gray"
    alpha: bool = True
    data: str
