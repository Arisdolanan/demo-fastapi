from fastapi import FastAPI
from version import __version__

from config import register_config,app
from routers import register_routers

app = FastAPI(
    title=app.service_title,
    description=app.service_description,
    summary=app.service_summary,
    version=__version__,
)

register_config(app)
register_routers(app)

@app.get("/")
def root():
    return {"message": "Welcome FastAPI is up and ok."}
