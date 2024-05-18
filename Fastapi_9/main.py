from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def add():
    return 5