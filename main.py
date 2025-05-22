from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Input(BaseModel):
    x: float
    y: float

@app.post("/add")
def add_numbers(data: Input):
    return {"result": data.x + data.y}
