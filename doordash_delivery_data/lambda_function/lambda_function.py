import boto3
import pandas as pd
from io import BytesIO
from io import StringIO
import json

landing_zone_bucket = "doordash-delivery-data-landing-zone"
target_zone_bucket = "doordash-delivery-data-target-zone"
doordash_sns_arn = 'arn:aws:sns:us-east-1:120582745863:doordashNotification'

s3_client = boto3.client("s3")
sns_client = boto3.client('sns')

def lambda_handler(event, context):
    try:
        # Read the content using pandas
        file_name = event['Records'][0]['s3']['object']['key']
        response = s3_client.get_object(Bucket=landing_zone_bucket, Key=file_name)
        file_content = response["Body"].read().decode('utf-8')
        data = json.loads(file_content)
        print((data))

        # processing data in the dataframe
        i = 0
        new_json_list = []
        for i in range(len(data)):
            print(data[i]['1'], data[i]['delivered'])
            if data[i]['delivered'] == 'delivered':
                new_json_list.append(data[i])

        # write json file back to s3
        json_str = json.dumps(new_json_list)
        s3_client.put_object(
            Bucket=target_zone_bucket,
            Key="delivered_" + file_name,
            Body=json_str,
        )

        message = "Input S3 File {} has been processed succesfuly !!".format("s3://" + landing_zone_bucket + "/" + file_name)
        respone = sns_client.publish(Subject="SUCCESS - Daily Data Processing", TargetArn=doordash_sns_arn, Message=message,
                                     MessageStructure='text')
    except Exception as err:
        print(err)
        message = "Input S3 File {} processing is Failed !!".format("s3://" + landing_zone_bucket + "/" + file_name)
        respone = sns_client.publish(Subject="FAILED - Daily Data Processing", TargetArn=doordash_sns_arn, Message=message,
                                     MessageStructure='text')