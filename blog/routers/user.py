from fastapi import APIRouter,Depends,status,HTTPException
from .. import schemas,models,database
from sqlalchemy.orm import Session
from .. hashin import Hash

router=APIRouter()

get_db=database.get_db
@router.post("/user",response_model=schemas.show_user,tags=["users"])
def create_user(req:schemas.User,db: Session=Depends(get_db)):
    
    new_user=models.user(name=req.name,email=req.email,password=Hash.bcrypt(req.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/user/{id}",response_model=schemas.show_user,tags=["users"])
def get_user(id:int,db:Session=Depends(get_db)):
    user=db.query(models.user).filter(models.user.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'user with the id {id} is not available')

    return user