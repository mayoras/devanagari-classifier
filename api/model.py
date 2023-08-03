from pydantic import BaseModel


class ImageBody(BaseModel):
    file: str
    colortype: str = "gray"
    alpha: bool = True
    data: str
