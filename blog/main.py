from fastapi import FastAPI, Depends
from .import schemas
from .import models
from .database import engine,session
from sqlalchemy.orm import Session 

app = FastAPI()

models.bas.metadata.create_all(engine)

def get_db():
    db=session()
    try:
        yield db
    finally:
        db.close() 

@app.post('/blog')
def create(req: schemas.Blog,db: Session=Depends(get_db)):
    new_blog=models.blog(title=req.title,body=req.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog
