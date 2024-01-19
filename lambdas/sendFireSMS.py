import json
import boto3

aws_region = "us-east-1"
phone_number = "+393801513777"

sns = boto3.client('sns', region_name=aws_region)

def lambda_handler(event, context):
    
    parking_space_id = event["parking_space_id"]
    
    sns.publish(
        PhoneNumber=phone_number,
        Message='Caution: Fire detected in parking space {}'.format(parking_space_id)
    )