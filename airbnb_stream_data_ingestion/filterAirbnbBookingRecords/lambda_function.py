import json
from datetime import datetime


def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)


def lambda_handler(event, context):
    # print("event-",event)
    # print("event[0]-",event[0])
    # print("json.dumps(event[0]-",json.dumps(event[0]) )
    # print("json.dumps(event[0]['body']-",json.dumps(event[0]['body']) )
    # print("json.loads(event[0]['body']-",json.loads(event[0]['body']) )

    print("event-", event)
    print("event[0]-", event[0])
    print("json.dumps(event[0])-", json.dumps(event[0]))
    print("json.loads(event[0]['body']-", json.loads(event[0]['body']))

    print("---------------------------------------------------------------")
    jsonData = json.loads(event[0]['body'])
    print(jsonData)
    print(type(jsonData))

    startDate = json.loads(event[0]['body'])['startDate']
    endDate = json.loads(event[0]['body'])['endDate']

    print("startDate", startDate)
    print("endDate", endDate)

    diff = days_between(startDate, endDate)
    if (diff > 1):
        print("----------------", json.loads(event[0]['body']))
        return jsonData