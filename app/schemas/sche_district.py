from typing import Optional, List

from pydantic import BaseModel, Field

from app.schemas.sche_base import BaseModelMappingFieldName


class DistrictRequest(BaseModelMappingFieldName):
    province_id: str = Field('', alias="provinceId")


class DistrictItem(BaseModelMappingFieldName):
    id: str
    code: str = ''
    name: Optional[str]
    region: Optional[str]
    province_id: Optional[str] = Field(None, alias="provinceId")


class DistrictDataResponse(BaseModel):
    districts: List[DistrictItem]
