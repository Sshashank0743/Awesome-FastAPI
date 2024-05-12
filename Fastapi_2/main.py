from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"hello":"world"}

@app.get("/next/{item_no}")
def root_2(item_no : int):
    return {"hello":item_no}

@app.get("/next2/{item_name}")
def root_2(item_name : str):
    return {"hello":item_name}