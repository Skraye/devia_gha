from fastapi import FastAPI

# init app
app = FastAPI()

@app.get("/")
def home():
    return "hello World!"

@app.get("/{number}")
def return_double(number: int):
    return get_double(number)

def get_double(number: int):
    return number * 2


@app.get("/2/{number}")
def return_double2(number: int):
    return get_double2(number)

def get_double2(number: int):
    return number * 2