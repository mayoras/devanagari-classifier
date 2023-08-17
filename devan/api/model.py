from typing import Literal
from pydantic import BaseModel, UUID4

ImageMode = Literal["gray", "rgb"]


class ImageBody(BaseModel):
    id: UUID4
    file: str
    mode: ImageMode = "gray"
    alpha: bool = True
    data: str
