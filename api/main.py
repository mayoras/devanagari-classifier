import os
import uvicorn
import fastapi as fapi

from typing import Annotated
from fastapi import FastAPI, Body, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware

from model import ImageBody

# define port number
PORT: int = int(os.getenv("DEVAN_API_PORT") or 8080)

# TODO: add prediction's module as a dependency
# instanciate FastAPI app object
app = FastAPI()

### MIDDLEWARES ###
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


### ROUTES ###
@app.get("/", status_code=200)
async def root():
    return {"message": "hello", "status": "ok"}


@app.post("/test")
async def test(body: Annotated[ImageBody, Body()]):
    print(body)
    return body


@app.post("/predict", status_code=fapi.status.HTTP_200_OK)
async def predict_example(
    img: Annotated[
        UploadFile,
        File(description="Input image with the handwritten character"),
    ] = ...
):
    return {"message": f"image {img.filename} received"}


### RUN ###
if __name__ == "__main__":
    try:
        uvicorn.run(
            app,
            host="localhost",
            port=PORT,
            log_level="debug",
            use_colors=True,
        )
    except:
        print("Error on start server.")
