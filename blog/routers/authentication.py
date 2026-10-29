from fastapi import APIRouter,Depends, HTTPException,status
from sqlalchemy.orm import Session
from .. import schemas,database,models,token
from fastapi.security import OAuth2PasswordRequestForm
from ..hashin import Hash
from datetime import datetime, timedelta, timezone
router = APIRouter(tags=["Authentication"])

@router.post("/login")
def login(request:OAuth2PasswordRequestForm=Depends(),db: Session=Depends(database.get_db)):
    user =db.query(models.user).filter(models.user.email==request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'invalid credentials')
    if not Hash.verify(user.password,request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'invalid credentials')

    access_token_expires = timedelta(minutes=30)
    access_token = token.create_access_token(
        data={"sub": user.email}
        
    )
    return {"access_token": access_token, "token_type": "bearer"}