import json

from app.helpers.read_s3_file import s3_helper


class ProvinceService(object):
    __instance = None
    province_file_path = 'province.json'

    def get_provinces(self):
        province_data = json.loads(s3_helper.read_s3_file(file_name=self.province_file_path))
        return province_data


province_srv = ProvinceService()
