from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn



app = FastAPI()

class Operation(BaseModel):
    a: float
    b: float

@app.get("/")
def homePage():
    return {'message': 'Welcome to our Calculator App'}

@app.post("/add")
def add(data: Operation):
    return {'result': data.a + data.b}

@app.post("/subtract")
def sub(data: Operation):
    return {'result': data.a - data.b}

@app.post("/multiply")
def mul(data: Operation):
    return {'result': data.a * data.b}

@app.post("/divide")
def div(data: Operation):
    if data.b == 0:
        return {"error": "Division by zero is not allowed"}
    return {"result": data.a / data.b}

@app.post("/square")
def square(data: Operation):
    return {"result": data.a ** data.b}

if __name__=="__main__":
    uvicorn.run(app="main:app", port=8000, reload=True, host="0.0.0.0")