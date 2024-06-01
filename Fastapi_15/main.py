from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Fruit(BaseModel):
    name : str
    count : int
    weight : Optional[int] = None


@app.get("/")
def hello():
    return {"hello":"world"}


@app.post("/fruit")
def fruits(f:Fruit):
    return {"name": f.name, "count":f.count}