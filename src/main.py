from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from api import router as api_router

app = FastAPI()

app.include_router(api_router, prefix="/frontend-api")

FRONTEND_DIST = Path(__file__).parent.parent / "frontend"
app.mount(
    "/",
    StaticFiles(directory=FRONTEND_DIST, html=True),
    name="frontend",
)
