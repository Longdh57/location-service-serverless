import json

from app.helpers.read_s3_file import s3_helper


class DistrictService(object):
    __instance = None
    district_file_path = 'district.json'

    def get_districts(self, province_id: str):
        all_district_data = json.loads(s3_helper.read_s3_file(file_name=self.district_file_path))
        districts = [district for district in all_district_data['districts'] if district['province_id'] == str(province_id)]
        return {'districts': districts}


district_srv = DistrictService()
