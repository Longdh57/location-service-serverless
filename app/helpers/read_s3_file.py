import logging

import boto3
from app.core.config import settings
from app.helpers.exception_handler import CustomException


class S3Helper(object):
    def __init__(self):
        self.s3 = boto3.resource('s3')
        self.s3_bucket = settings.S3_BUCKET

    def read_s3_file(self, file_name: str = None):
        try:
            obj = self.s3.Object(self.s3_bucket, file_name)
            body = obj.get()['Body'].read()
            return body.decode("utf-8")
        except Exception as e:
            logging.error(e)
            raise CustomException(http_code=400, code='400', message=str(e))


s3_helper = S3Helper()
