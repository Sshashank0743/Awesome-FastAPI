from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/")
def hello():
    return {"hello":"world"}

# @app.get("/fruit/{fruit_name}/count/{fruit_count}/weight/{fruit_weight}")
# def fruit(fruit_name : str, fruit_count : int, fruit_weight : str):
#     return{"fruit name": fruit_name, "total count": fruit_count, "total weight": fruit_weight}


@app.get("/fruit/{fruit_name}/count/{fruit_count}")
def fruit(fruit_name : str, fruit_count : int, fruit_weight : Optional[str]):
    return{"fruit name": fruit_name, "total count": fruit_count, "total weight": fruit_weight}