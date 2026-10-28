from fastapi import APIRouter,Depends, HTTPException,status
from sqlalchemy.orm import Session
from .. import schemas,database,models
from ..hashin import Hash
router = APIRouter(tags=["Authentication"])

@router.post("/login")
def login(request:schemas.Login,db: Session=Depends(database.get_db)):
    user =db.query(models.user).filter(models.user.email==request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'invalid credentials')
    if not Hash.verify(user.password,request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'invalid credentials')

    return user