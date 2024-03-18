import json
from random import randint
import random
import datetime
from datetime import date, timedelta
import boto3
from faker import Faker
import uuid

QUEUE_URL = 'https://sqs.us-east-1.amazonaws.com/120582745863/AirbnbBookingQueue'
sqs_client = boto3.client("sqs")

def lambda_handler(event, context):
    myGenerator = Faker()
    myGenerator.random.seed(1234)
    def generate_booking_data(i):
        startDate =  datetime.datetime.strptime(myGenerator.date(),'%Y-%m-%d').date()
        endDate = startDate
        if ( i % 3 == 0):
            endDate = startDate + timedelta(5)
        else:
            endDate = startDate + timedelta(1)

        return {
                "bookingId": str(uuid.uuid4()),
                "userId": str(randint(0,10000)),
                "propertyId": str(randint(0,10000) * 9000),
                "location": str(myGenerator.state() + ','  + myGenerator.country()),
                "startDate": "{}".format(startDate),
                "endDate": "{}".format(endDate),
                "price": random.uniform(0,10000)
        }

    for i in range(10):
        payload = json.dumps(generate_booking_data(i))
        print(payload)
        sqs_client.send_message(
            QueueUrl=QUEUE_URL,
            MessageBody=payload)