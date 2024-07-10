from fastapi import FastAPI, Query
from typing import Optional

app = FastAPI()

@app.get("/")
def hello():
    return {"hello":"world"}


@app.get("/fruit/")
def Fruits(fruit_name: Optional[str] = Query(None, max_length=5)):
    return {"This is query parameters additional option":fruit_name}


@app.get("/fruit1/")
def Fruits(fruit_name: str = Query(..., min_length=2, max_length=5)):
    return {"This is query parameters additional option":fruit_name}


@app.get("/fruit2/")
def Fruits(fruit_name: Optional[str] = Query("orange", min_length=2, max_length=5)):
    a = 2
    if fruit_name:
        print("Optional parameters are available")
    return {"This is query parameters additional option":a}