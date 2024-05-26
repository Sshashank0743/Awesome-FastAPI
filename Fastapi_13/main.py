from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello():
    return{"Hello":"world"}
@app.get("/fruit")
def fruit(name: str, weight: str):
    return {"Fruit_name ": name, "Fruit_weight": weight}


@app.get("/fruit1")
def fruit(count: int, weight: int):
    return {"Fruit_count": count, "Fruit_weight": weight}