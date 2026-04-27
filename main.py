from fastapi import FastAPI

app = FastAPI()
@app.get("/blog")
def index(limi=10, published: bool = True, sort: str = None):
    if published:
     return f"{limi} publish"
    else:
        return f"{limi} not publish"

@app.get("/blog/{id}")
def show(id: int):
    return {"data": id}    
