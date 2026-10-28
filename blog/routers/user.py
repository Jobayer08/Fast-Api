from fastapi import APIRouter,Depends,status
from .. import schemas,models,database
from sqlalchemy.orm import Session
from ..repository import user

router=APIRouter(
    prefix="/user",
    tags=["Users"]
    )

get_db=database.get_db
@router.post("/",response_model=schemas.show_user)
def create_user(req:schemas.User,db: Session=Depends(get_db)):
    return user.create(req,db)
    

@router.get("/{id}",response_model=schemas.show_user)
def get_user(id:int,db:Session=Depends(get_db)):
   return user.show(id,db)