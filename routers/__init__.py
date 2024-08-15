from fastapi import FastAPI
from controllers import hello_controller, book_controller

def register_routers(app: FastAPI):
    app.include_router(hello_controller.router,prefix="/api/v1", tags=["Hello"])
    app.include_router(book_controller.router,prefix="/api/v1", tags=["Books"])
