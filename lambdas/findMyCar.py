import boto3
from boto3.dynamodb.conditions import Key, Attr

def lambda_handler(event, context):
    # Get the input string from the event
    number_plate = event['number_plate']

    dynamodb = boto3.resource('dynamodb')
    parking_table = dynamodb.Table('parking')

    items = parking_table.scan(FilterExpression=Attr('number_plate').contains(number_plate))

    if len(items['Items']) == 1:
        return {
            'statusCode': 200,
            'body': {
                'items': items['Items']
            }
        }
        
    return {
            'statusCode': 404,
            'body': {
                'error': 'No or more than one car was found'
            }
        }