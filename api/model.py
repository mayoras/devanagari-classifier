from pydantic import BaseModel


class ImageBody(BaseModel):
    file: str
    mode: str = "gray"
    alpha: bool = True
    data: str
