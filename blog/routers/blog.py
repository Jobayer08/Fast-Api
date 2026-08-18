from fastapi import APIRouter,Depends, HTTPException,status
from .. import schemas,database,models
from typing import List
from sqlalchemy.orm import Session 

get_db=database.get_db

router = APIRouter()

@router.get('/blog',response_model=list[schemas.ShowBlog],tags=["Blogs"])
def all(db: Session=Depends(database.get_db)):
    blogs=db.query(models.blog).all()
    return blogs

@router.post('/blog',status_code=status.HTTP_201_CREATED,tags=["Blogs"])
def create(req: schemas.Blog,db: Session=Depends(get_db)):
    new_blog=models.blog(title=req.title,body=req.body,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@router.delete('/blog/{id}',status_code=status.HTTP_204_NO_CONTENT,tags=["Blogs"])
def destroy(id,db: Session=Depends(get_db)):
    blog=db.query(models.blog).filter(models.blog.id==id)
    if not blog.first():
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with the id {id} is not available')
    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'
@router.put('/blog/{id}',status_code=status.HTTP_202_ACCEPTED,tags=["Blogs"])
def update(id,req: schemas.Blog,db: Session=Depends(get_db)):
    blog=db.query(models.blog).filter(models.blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with the id {id} is not available')
    blog.update(req.dict())
    db.commit()
    return 'updated'   

@router.get('/blog/{id}',status_code=200,response_model=schemas.ShowBlog,tags=["Blogs"])
def show(id,db: Session=Depends(get_db)):
    blog=db.query(models.blog).filter(models.blog.id==id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with the id {id} is not available')
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail': f'Blog with the id {id} is not available'}
    return blog

