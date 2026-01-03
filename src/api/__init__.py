from fastapi import APIRouter

from .sites import router as sites_router
from .users import router as users_router

router = APIRouter()
router.include_router(users_router, prefix="/users", tags=["users"])
router.include_router(sites_router, prefix="/sites", tags=["sites"])
