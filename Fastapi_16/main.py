from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/")
def hello():
    return {"hello":"world"}


@app.get("/fruit")
def Fruits(fruit_name: Optional[str] = None):
    return {"This is query parameters additional option":fruit_name}