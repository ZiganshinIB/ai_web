from fastapi import FastAPI

from .sites import sites_router
from .users import users_router


def get_app() -> FastAPI:
    app = FastAPI(
        title="Frontend API",
        version="1.0.0",
        docs_url="/docs",
        openapi_url="/openapi.json",
    )

    app.include_router(users_router, prefix="/users", tags=["Users"])
    app.include_router(sites_router, prefix="/sites", tags=["Sites"])
    return app
