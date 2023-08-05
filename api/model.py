from typing import Literal
from pydantic import BaseModel


class ImageBody(BaseModel):
    file: str
    mode: Literal["gray", "rgb"] = "gray"
    alpha: bool = True
    data: str
