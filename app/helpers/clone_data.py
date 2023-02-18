import json
import pathlib
import time

import boto3
from requests import request

headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
}


def clone_province():
    response = request(
        method='get', url='https://location-v2.tekoapis.com/api/v1/location/provinces', headers=headers, timeout=60)
    data = response.json()['result']
    file_path = str(pathlib.Path(__file__).parent.resolve()) + '/province.json'
    f = open(file_path, "w")
    f.write(json.dumps(data))
    f.close()


def clone_district():
    provinces = request(
        method='get', url='https://location-v2.tekoapis.com/api/v1/location/provinces', headers=headers).json()['result']['provinces']


    districts = []
    for province in provinces:
        print(f'[x] ProvinceId: {province["id"]}')
        response = request(
            method='get',
            url=f'https://location-v2.tekoapis.com/api/v1/location/districts?provinceId={province["id"]}',
            headers=headers,
            timeout=60
        )
        data = response.json()['result']['districts']
        for district in data:
            district['province_id'] = province["id"]
        districts += data

        file_path = str(pathlib.Path(__file__).parent.resolve()) + '/district.json'
        f = open(file_path, "w")
        f.write(json.dumps(districts))
        f.close()
        time.sleep(1)


def clone_ward():
    s3 = boto3.resource('s3')
    obj = s3.Object('location-service-serverless', 'district.json')
    body = obj.get()['Body'].read()
    all_district_data = json.loads(body.decode("utf-8"))
    wards = []
    for district in all_district_data['districts']:
        print(f'[x] district: {district["id"]}')
        response = request(
            method='get',
            url=f'https://location-v2.tekoapis.com/api/v1/location/wards?districtId={district["id"]}',
            headers=headers,
            timeout=60
        )
        if response.json()['result'].get('wards'):
            data = response.json()['result']['wards']
            for ward in data:
                ward['district_id'] = ward["districtId"]
                ward['province_id'] = ward["provinceId"]
            wards += data

        file_path = str(pathlib.Path(__file__).parent.resolve()) + '/wards.json'
        f = open(file_path, "w")
        f.write(json.dumps(wards))
        f.close()
        time.sleep(1)


clone_ward()
