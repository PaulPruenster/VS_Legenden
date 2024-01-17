import boto3
import json

# example request body:
# {
#   "key": "fire.jpeg",
#   "bucket": "verteiltesystemeparkingsystem2"
# }

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    rekognition = boto3.client('rekognition')

    bucket = event['bucket']
    key = event['key']

    obj = s3.get_object(Bucket=bucket, Key=key)
    image = obj['Body'].read()

    response = rekognition.detect_labels(Image={'Bytes': image})

    labels = []
    for label in response['Labels']:
        labels.append({
            'Name': label['Name'],
            'Confidence': label['Confidence']
        })

    return json.dumps(labels)
