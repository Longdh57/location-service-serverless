from typing import Optional, List

from pydantic import BaseModel, Field

from app.schemas.sche_base import BaseModelMappingFieldName


class WardRequest(BaseModelMappingFieldName):
    district_id: str = Field('', alias="districtId")


class WardItem(BaseModelMappingFieldName):
    id: str
    code: str = ''
    name: Optional[str]
    region: Optional[str]
    district_id: Optional[str] = Field(None, alias="districtId")
    province_id: Optional[str] = Field(None, alias="provinceId")


class WardDataResponse(BaseModel):
    wards: List[WardItem]
