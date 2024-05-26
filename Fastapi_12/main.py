from enum import Enum

from fastapi import FastAPI

class Fruits(str, Enum):
    orange = "orange"
    apple = "apple"
    grapes = "grapes"

app = FastAPI()

@app.get("/fruits/{fruit_name}")
def get_fruit(fruit_name : Fruits):
    if fruit_name == fruit_name.orange:
        return{"fruit name is matched": fruit_name}

    if fruit_name == fruit_name.apple:
        return {"fruit name is matched": fruit_name}

    return{"fruit name": fruit_name}