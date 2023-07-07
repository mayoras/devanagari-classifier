import os
import uvicorn
from typing import Annotated
from fastapi import FastAPI, Path

# define port number
PORT: int = int(os.getenv("DEVAN_API_PORT") or 8080)

# instanciate FastAPI app object
app = FastAPI()


### ROUTES ###
@app.get("/test/{test_id}")
async def test(test_id=Annotated[int, Path(description="Just a test ID")]):
    return test_id


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
