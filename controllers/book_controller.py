from fastapi import APIRouter
from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from database.mysql_db import db_dependency
from pydantic import PositiveInt
from models.book import BookModel
from fastapi.encoders import jsonable_encoder
from schemas.book import BookCreate,BookUpdate

router = APIRouter(
    prefix="/book",
    tags=["Books"]
)

@router.get("/")
def get_books(
    db: db_dependency,
    limit: PositiveInt = 10,
):
    res = db.query(BookModel).limit(limit).all()
    if res:
        return JSONResponse(status_code=status.HTTP_200_OK, content= {"status":status.HTTP_200_OK,"data":jsonable_encoder(res)})
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="data book not found")

@router.get("/{id}")
def get_book(db: db_dependency, id: int):
    res = db.query(BookModel).filter(BookModel.id == id).first()
    if res:
        return JSONResponse(status_code=status.HTTP_200_OK, content= {"status":status.HTTP_200_OK,"data":jsonable_encoder(res)})
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"book with id: {id} not found.")

@router.post("/")
def create_book(db: db_dependency, item: BookCreate):
    db_book = BookModel(**item.dict())
    if db_book is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="book not found")
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content={"status":status.HTTP_201_CREATED,"data": f'book with id: {db_book.id} created successfully'})

@router.put("/")
def update_book(db: db_dependency, id: int, item: BookUpdate):
    db_book = db.query(BookModel).filter(BookModel.id == id).first()

    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")

    update_data = item.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_book, key, value)

    db.commit()
    db.refresh(db_book)
    return JSONResponse(status_code=status.HTTP_200_OK, content={"status":status.HTTP_200_OK,"data": f'book with id: {db_book.id} updated successfully'})

@router.delete("/{id}")
def delete_book(id: int, db: db_dependency):
    db_book = db.query(BookModel).filter(BookModel.id == id).first()
    if db_book is None:
        raise HTTPException(status_code=404, detail="book not found")
    db.delete(db_book)
    db.commit()
    return JSONResponse(status_code=status.HTTP_200_OK, content= {"status":status.HTTP_200_OK,"data": f'book with id: {id} deleted successfully'})
