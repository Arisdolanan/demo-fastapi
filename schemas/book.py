from sqlalchemy import Column, Integer, String, Text, Date
from typing import Optional
from pydantic import BaseModel, validator
from datetime import datetime

class BookBase(BaseModel):
        name: str
        category: Optional[str] = None
        publisher: str
        number_of_pages: int
        start_reading: Optional[str] = None
        end_reading: Optional[str] = None

        @validator('start_reading')
        def parse_start_reading(cls, v):
            return datetime.strptime(v, '%d-%m-%Y')

        @validator('end_reading')
        def parse_end_reading(cls, v):
            return datetime.strptime(v, '%d-%m-%Y')

class BookCreate(BookBase):
    pass

class BookResponse(BookBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

class BookUpdate(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    publisher: Optional[str] = None
    number_of_pages: Optional[int] = None
    start_reading: Optional[datetime] = None
    end_reading: Optional[datetime] = None
