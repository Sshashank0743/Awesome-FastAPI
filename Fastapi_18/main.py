from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.get("/")
def hello():
    return {"hello":"world"}

@app.post("/file")
def create_f(file: bytes = File(...)):
    return {"file size":len(file)}


@app.post("/uploaded_f")
def uploaded_f(file:UploadFile):
    return {"filename":file.filename}