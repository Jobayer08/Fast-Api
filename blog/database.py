from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_UR = "sqlite:///./blog.db"


engine = create_engine(SQLALCHEMY_DATABASE_UR, connect_args={"check_same_thread": False})

session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

bas = declarative_base()