from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

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


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

@app.post("/blog")
def create_blog(requst: Blog):   
    return {"data": requst.title} 
   