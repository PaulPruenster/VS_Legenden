import boto3
from boto3.dynamodb.conditions import Key, Attr

# example request body:
# {
#   "number_plate": "test123"
# }

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    parking_table = dynamodb.Table('parking')
    
    number_plate = event['number_plate']

    items = parking_table.scan(FilterExpression=Attr('number_plate').eq(number_plate))

    return {
        'statusCode': 200,
        'body': items['Items'][0]['parking_id']
    }