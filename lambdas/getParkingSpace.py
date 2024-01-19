import boto3
import json
from boto3.dynamodb.conditions import Key, Attr

# example request body:
# {}


def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    parking_table = dynamodb.Table('parking')

    items = parking_table.scan(FilterExpression=Attr('is_empty').eq(True))
    for i in range(len(items['Items'])):
        items['Items'][i]['parking_id'] = int(items['Items'][i]['parking_id'])
    print(items)

    # Create the response payload
    response = {
        'statusCode': 200,
        'body': json.dumps({
            'items': items['Items']
        })
    }

    return response
