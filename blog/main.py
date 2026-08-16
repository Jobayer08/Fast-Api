from fastapi import FastAPI, Depends,status,Response,HTTPException
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

@app.post('/blog',status_code=status.HTTP_201_CREATED)
def create(req: schemas.Blog,db: Session=Depends(get_db)):
    new_blog=models.blog(title=req.title,body=req.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.delete('/blog/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destroy(id,db: Session=Depends(get_db)):
    blog=db.query(models.blog).filter(models.blog.id==id)
    if not blog.first():
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with the id {id} is not available')
    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'

@app.put('/blog/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id,req: schemas.Blog,db: Session=Depends(get_db)):
    blog=db.query(models.blog).filter(models.blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with the id {id} is not available')
    blog.update(req.dict())
    db.commit()
    return 'updated'    


@app.get('/blog',response_model=list[schemas.ShowBlog])
def all(db: Session=Depends(get_db)):
    blogs=db.query(models.blog).all()
    return blogs

@app.get('/blog/{id}',status_code=200,response_model=schemas.ShowBlog)
def show(id,response: Response,db: Session=Depends(get_db)):
    blog=db.query(models.blog).filter(models.blog.id==id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with the id {id} is not available')
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail': f'Blog with the id {id} is not available'}
    return blog

@app.post("/user")
def create_user(req:schemas.User,db: Session=Depends(get_db)):
    new_user=models.user(name=req.name,email=req.email,password=req.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user