from fastapi import FastAPI
import schemas
import models
from database import engine

app = FastAPI()

models.bas.metadata.create_all(engine)

@app.post('/blog')
def create(req: schemas.Blog):
    return req
