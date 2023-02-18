import json

from app.helpers.read_s3_file import s3_helper


class WardService(object):
    __instance = None
    ward_file_path = 'ward.json'

    def get_wards(self, district_id: str):
        all_ward_data = json.loads(s3_helper.read_s3_file(file_name=self.ward_file_path))
        wards = [ward for ward in all_ward_data['wards'] if ward['district_id'] == str(district_id)]
        return {'wards': wards}


ward_srv = WardService()
