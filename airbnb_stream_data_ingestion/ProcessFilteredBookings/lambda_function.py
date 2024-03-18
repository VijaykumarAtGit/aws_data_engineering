import json
import boto3
import random

bucket_name = 'airbnb-booking-records-airbnb'
s3_client = boto3.client("s3")


def lambda_handler(event, context):
    print(event)
    print(event[0])
    data = json.dumps(event[0])
    num = event[0]['userId']

    s3_client.put_object(Body=data, Bucket=bucket_name, Key=str(num) + '_airAnbRecords.txt')


