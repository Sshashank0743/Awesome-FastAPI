from fastapi import FastAPI, HTTPException

app = FastAPI()

fruit = {"orange":"This fruit is sour"}

@app.get("/")
def hello():
    return {"hello":"fruit"}

@app.get("/fruits/{fruit_name}")
def read_fruit(fruit_name: str):
    if fruit_name not in fruit:
        raise HTTPException(status_code=404, detail = "Item not found")
    return {"fruit property is: ":fruit[fruit_name]}