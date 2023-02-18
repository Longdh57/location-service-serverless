from fastapi import APIRouter

from app.api import api_healthcheck, api_location

router = APIRouter()

router.include_router(api_location.router, tags=["location"], prefix="")
router.include_router(api_healthcheck.router, tags=["health-check"], prefix="/healthcheck")
