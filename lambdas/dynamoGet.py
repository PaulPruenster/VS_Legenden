import boto3
from boto3.dynamodb.conditions import Key, Attr

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    parking_table = dynamodb.Table('parking')

    items = parking_table.scan(FilterExpression=Attr('is_empty').eq(True))

    return {
        'statusCode': 200,
        'body': {
            'items': items['Items']
        }
    }
