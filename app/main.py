import logging
from typing import Optional

import uvicorn
from fastapi import FastAPI
from mangum import Mangum

from app.api.api_router import router
from app.api import api_location
from app.core.config import settings
from app.helpers.exception_handler import CustomException, http_exception_handler

logging.config.fileConfig(settings.LOGGING_CONFIG_FILE, disable_existing_loggers=False)


def get_application(api_point: Optional[str] = None) -> FastAPI:
    application = FastAPI(
        title=settings.PROJECT_NAME, docs_url="/docs", redoc_url='/re-docs',
        openapi_url=f"{settings.API_PREFIX}/openapi.json",
        description='''
        VietNam Location Service  
        Includes API province, district and ward
        '''
    )
    if api_point == 'province':
        application.include_router(api_location.router_province, prefix=settings.API_PREFIX)
    elif api_point == 'district':
        application.include_router(api_location.router_district, prefix=settings.API_PREFIX)
    elif api_point == 'ward':
        application.include_router(api_location.router_ward, prefix=settings.API_PREFIX)
    else:
        application.include_router(router, prefix=settings.API_PREFIX)
    application.add_exception_handler(CustomException, http_exception_handler)

    return application


app = get_application()
if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)

handler_province = Mangum(get_application(api_point='province'))
handler_district = Mangum(get_application(api_point='district'))
handler_ward = Mangum(get_application(api_point='ward'))
