from fastapi import APIRouter, Depends

from app.schemas.sche_base import DataResponse
from app.schemas.sche_district import DistrictDataResponse, DistrictRequest
from app.schemas.sche_province import ProvinceDataResponse
from app.schemas.sche_ward import WardDataResponse, WardRequest
from app.services.srv_province import province_srv
from app.services.srv_district import district_srv
from app.services.srv_ward import ward_srv

router_province = APIRouter()
router_district = APIRouter()
router_ward = APIRouter()


@router_province.get("/provinces", response_model=DataResponse[ProvinceDataResponse])
async def get():
    data = province_srv.get_provinces()
    return {"data": data}


@router_district.get("/districts", response_model=DataResponse[DistrictDataResponse])
async def get(params: DistrictRequest = Depends()):
    data = district_srv.get_districts(province_id=params.province_id)
    return {"data": data}


@router_ward.get("/wards", response_model=DataResponse[WardDataResponse])
async def get(params: WardRequest = Depends()):
    data = ward_srv.get_wards(district_id=params.district_id)
    return {"data": data}
