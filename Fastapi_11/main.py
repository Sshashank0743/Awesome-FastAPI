## Define item type

from fastapi import FastAPI

app = FastAPI()


@app.get("/{item}")
def show_item(item : str):
    return {"items": item}