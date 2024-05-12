from fastapi import FastAPI


app =  FastAPI()


@app.get("/")
def typeHint(name: str, height: int):
    start_name = "Your name is "+ name
    last_name = " and your last name is "+ height
    full_name = start_name.title() + last_name.title()
    return full_name

print(typeHint("shashank", "shukla"))