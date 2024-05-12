from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root_get():
    return {"1":"2"}


#This method will through an error, I have explained in text file why?
@app.put("/hello")
def root_put():
    return {"1":"2"}