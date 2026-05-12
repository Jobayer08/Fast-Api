from database import bas
from sqlalchemy import Column, Integer, String

class blog(bas):
    id = Column(Integer, primary_key=True, index=True)
    title=Column(String)
    body=Column(String)
