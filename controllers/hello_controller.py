from fastapi import APIRouter

router = APIRouter(
    prefix="/hello",
    tags=["Hello"]
)

@router.get("/me")
async def get_me():
    return {"message": "Hello World"}
