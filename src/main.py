from pathlib import Path

from fastapi import APIRouter, FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Ваши маршруты
router = APIRouter()


# Пример маршрута
@router.get("/test")
async def index():
    return {"message": "Hello World"}


app.include_router(router)

# Подключение фронтенда
FRONTEND_DIST = Path(__file__).parent.parent / "frontend"
# Статика (js, css, assets)
app.mount(
    "/assets",
    StaticFiles(directory=FRONTEND_DIST / "assets"),
    name="assets",
)


# SPA fallback (React Router)
@app.get("/{full_path:path}")
def serve_react_app(full_path: str):
    return FileResponse(FRONTEND_DIST / "index.html")
