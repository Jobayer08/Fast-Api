from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException, status

def get_all(db:Session):
    blogs=db.query(models.blog).all()
    return blogs

def creat(req: schemas.Blog,db: Session):
    new_blog=models.blog(title=req.title,body=req.body,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def destroy(id:int,db: Session):
    blog=db.query(models.blog).filter(models.blog.id==id)
    if not blog.first():
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with the id {id} is not available')
    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'

def update(id:int,req: schemas.Blog,db: Session):
    blog=db.query(models.blog).filter(models.blog.id==id)
    if not blog.first():
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with the id {id} is not available')
    blog.update(req.dict())
    db.commit()
    return 'updated' 

def show(id:int,db: Session):
    blog=db.query(models.blog).filter(models.blog.id==id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with the id {id} is not available')
            # response.status_code = status.HTTP_404_NOT_FOUND
            # return {'detail': f'Blog with the id {id} is not available'}
    return blog