import boto3
import json
import datetime
import base64
"""
json body should look like:
{
    "id": 10,
    "image": "/9j/2wBDAAg ...." < base64 encoded image
}

"""
s3 = boto3.client('s3')
client = boto3.client('stepfunctions')
bucket_name = "verteiltesystemeparkingsystem"
state_machine_arn = 'arn:aws:states:us-east-1:798389635088:stateMachine:MyStateMachine-oskxiinvr'


def lambda_handler(event, context):
    # load json data from body
    body = json.loads(event['body'])
    parking_space_id = body['id']

    # image should be send in base64
    image_decoded = base64.b64decode(body['image'])
    if image_decoded:
        image_buffer = bytearray(image_decoded)

    # create the image file name
    now = datetime.datetime.now()
    timestamp_string = now.strftime("%Y-%m-%dT%H:%M:%S")
    image_key = f"{parking_space_id}_{timestamp_string}.jpg"

    # safe the image to the bucket
    s3.put_object(Body=image_buffer, Bucket=bucket_name, Key=image_key)

    # create the URL for the image
    image_url = f"https://{bucket_name}.s3.amazonaws.com/{image_key}"

    # Create a Step Functions client
    client = boto3.client('stepfunctions')

    step_function_request = {
        "url": image_url,
        "id": 10,
    }

    response = client.start_execution(
        stateMachineArn=state_machine_arn,
        input=json.dumps(step_function_request)
    )

    response = {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Image was uploaded."
        })
    }
    return response
