from .database import bas
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

class blog(bas):
    __tablename__ = 'blogs'
    id = Column(Integer, primary_key=True, index=True)
    title=Column(String)
    body=Column(String)
    user_id=Column(Integer, ForeignKey("users.id"))

    creator=relationship("user", back_populates="blogs")

class user(bas):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name=Column(String)
    email=Column(String)
    password=Column(String)  

    blogs=relationship("blog", back_populates="creator") 


