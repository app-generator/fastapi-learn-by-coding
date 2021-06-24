from fastapi import FastAPI

from enum import Enum

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

app = FastAPI()

# Basic Hello World
@app.get("/")
async def root():
    return {"message": "Hello FastAPI"}

# Integer Validation
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

# Enum use
@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}
