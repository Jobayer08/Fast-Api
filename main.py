from fastapi import FastAPI

app = FastAPI()
@app.get("/")
def index():
    return "Hello, World!"

@app.get("/blog/{id}")
def show(id: int):
    return {"data": id}    
