import boto3
from boto3.dynamodb.conditions import Key, Attr

# example request body:
# {
#   "id": 0,
#   "is_empty": "true"
# }


def lambda_handler(event, context):
    # Get the DynamoDB client
    dynamodb = boto3.resource('dynamodb')

    # Get the parking table
    parking_table = dynamodb.Table('parking')

    # Get the id of the item to insert
    id = event['id']
    is_empty = event['is_empty']

    response = parking_table.update_item(
        Key={'parking_id': id},
        UpdateExpression="set is_empty = :r",
        ExpressionAttributeValues={
            ':r': is_empty,
        },
        ReturnValues="UPDATED_NEW"
    )

    # Return a success response
    return {
        'statusCode': 200,
        'body': 'Item inserted successfully'
    }
