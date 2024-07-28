from fastapi import FastAPI
from config import cors

def register_config(app: FastAPI):
    cors.add(app)
