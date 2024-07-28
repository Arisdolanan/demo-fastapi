from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func

from database.mysql_db import Base

class BookModel(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    category = Column(String(50))
    publisher = Column(String(50))
    number_of_pages = Column(Integer)
    start_reading = Column(DateTime)
    end_reading = Column(DateTime)
    created_at = Column(DateTime(timezone=True), default=func.now())
