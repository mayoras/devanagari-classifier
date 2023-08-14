import uvicorn
import fastapi as fapi

from typing import Annotated
from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware

from devan.api.model import ImageBody
from devan.api.image import parse_image
from devan.constants.api import DEVAN_API_PORT, DEVAN_API_HOSTNAME, DEVAN_PROD_ENV

from devan.character import Character

# define hostname and port number
HOSTNAME: str = DEVAN_API_HOSTNAME
PORT: int = DEVAN_API_PORT

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


@app.post("/predict", status_code=fapi.status.HTTP_200_OK)
async def predict_example(body: Annotated[ImageBody, Body()]):
    img = parse_image(body)

    # Instance a character object
    user_char = Character(pil_img=img)

    user_char.show_character()

    # Instance a pipeline

    # Return the final response

    return {"message": f"image {body.file} received"}


### RUN ###
if __name__ == "__main__":
    try:
        uvicorn.run(
            app,
            host=HOSTNAME,
            port=PORT,
            log_level="debug" if not DEVAN_PROD_ENV else "None",
            use_colors=True,
        )
    except:
        print("Error on start server.")
