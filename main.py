import uvicorn
import fastapi as fapi

from typing import Annotated, List

from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware

from devan.api.model import ImageBody
from devan.api.image import parse_image
from devan.constants.api import DEVAN_API_PORT, DEVAN_API_HOSTNAME, DEVAN_PROD_ENV
from devan.constants.model import DEVAN_MODEL_FILENAME
from devan.character import Character
from devan.pipeline import Pipeline, TransformList
from devan.preproc import min_max_scaling, get_hog_desc
from devan.model import load_model, label_to_char_name

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
async def predict_example(body: Annotated[List[ImageBody], Body()]):
    imgs = [parse_image(ib) for ib in body]

    # Instance a character object
    user_chars = [Character(id=id, pil_img=img) for (id, img) in imgs]

    # user_char.save_character_image("./data/images/test.png")

    # Instance a pipeline and add the transforms in order
    transforms: TransformList = [
        (min_max_scaling, {"min_vals": None, "max_vals": None}),
        (get_hog_desc, {}),
    ]
    pipeline = Pipeline(chars=user_chars, trans=transforms)

    pipeline.transform()

    # load model
    model = load_model(DEVAN_MODEL_FILENAME)
    pipeline.model = model

    # Predict user character
    pred = pipeline.predict()

    # Return the final response
    labels = {
        f"{c.id}": label_to_char_name(label) for (c, label) in zip(user_chars, pred)
    }

    return {"success": True, "labels": labels}


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
