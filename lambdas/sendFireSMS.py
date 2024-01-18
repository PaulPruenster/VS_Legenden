import json
import boto3

aws_region = "us-east-1"
phone_number = "+393409590100"

sns = boto3.client('sns', region_name=aws_region)

def send_sms(id):
    sns.publish(
        PhoneNumber=phone_number,
        Message='Caution: Fire detected in parking space {}'.format(id)
    )