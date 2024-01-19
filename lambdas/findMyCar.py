import boto3
import json
from boto3.dynamodb.conditions import Key, Attr

  
def lambda_handler(event, context):
    print("start")
    print(event)
    if 'body' not in event:
        return {
            "statusCode": 400,
            "body": json.dumps({
                "message": "no body was send."
            })
        }

    # load json data from body
    body = json.loads(event['body'])

    if 'number_plate' not in body:
        return {
            "statusCode": 400,
            "body": json.dumps({
                "message": "number_plate or image missing."
            })
        }

    number_plate = body['number_plate']
    print(number_plate)

    dynamodb = boto3.resource('dynamodb')
    parking_table = dynamodb.Table('parking')

    items = parking_table.scan(FilterExpression=Attr(
        'number_plate').contains(number_plate))
    if len(items['Items']) == 1:
        print(items['Items'][0])
        items['Items'][0]['parking_id'] = int(items['Items'][0]['parking_id'])
        response = {
            "statusCode": 200,
            "body": json.dumps({
                "message": "car was found",
                "item": items['Items'][0]
            })
        }

        print(response)

        return response

    return {
        "statusCode": 400,
        "body": json.dumps({
            "message": "No or more than one car was found"
        })
    }
