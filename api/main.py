import os
import uvicorn
import fastapi as fapi

from typing import Annotated
from fastapi import FastAPI, Path, UploadFile, File

# define port number
PORT: int = int(os.getenv("DEVAN_API_PORT") or 8080)

# TODO: add prediction's module as a dependency
# instanciate FastAPI app object
app = FastAPI()


### ROUTES ###
@app.get("/test/{test_id}")
async def test(test_id: Annotated[int, Path(description="Just a test ID")]):
    return test_id


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
