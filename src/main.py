from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from frontend_api.app import get_app

app = FastAPI()

MEDIA_DIR = Path(__file__).parent.parent / "media"
app.mount("/media", StaticFiles(directory=MEDIA_DIR), name="media")

app.mount("/frontend-api", get_app(), name="frontend-api")

FRONTEND_DIST = Path(__file__).parent.parent / "frontend"
app.mount(
    "/",
    StaticFiles(directory=FRONTEND_DIST, html=True),
    name="frontend",
)
