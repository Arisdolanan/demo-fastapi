from fastapi import Depends
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,Session
from typing import Annotated

# SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:root@localhost:3307/db_book"
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:root@host.docker.internal:3307/db_book"

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
meta = MetaData()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]
