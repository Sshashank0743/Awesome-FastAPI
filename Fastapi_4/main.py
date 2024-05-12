from fastapi import FastAPI
from pydantic import BaseModel


class Fruit(BaseModel):
    name: str
    price: int


app = FastAPI()


@app.get("/")
def root_default():
    return {"hello": "world"}


@app.get("/fruit_count/{count}")
def root_get_count(count: int):
    return {"Total fruit count": count}


@app.put("/fruit_count_1/{count}")
def root_get_count(count: int, fruit_name: Fruit):
    return {"Total fruit count is": count, "and the fruit name is": fruit_name.name, "having price": fruit_name.price}
