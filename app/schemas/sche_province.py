from typing import Optional, List

from pydantic import BaseModel


class ProvinceItem(BaseModel):
    id: str
    code: str = ''
    name: Optional[str]
    region: Optional[str]

    class Config:
        orm_mode = True


class ProvinceDataResponse(BaseModel):
    provinces: List[ProvinceItem]
