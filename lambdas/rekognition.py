import boto3
import json

"""
 example request body:
{
    "image_key": "fire.jpeg",
    "parking_space_id": 10
}
"""

aws_region = "us-east-1"
phone_number = "+393409590100"

sns = boto3.client('sns', region_name=aws_region)

bucket = 'verteiltesystemeparkingsystem'
fire_words = ['fire', 'flames']
car_words = ['car', "license plate", "vehicle", "transportation"]

def send_sms(message):
    sns.publish(
        PhoneNumber=phone_number,
        Message=message
    )


def lambda_handler(event, context):
    s3 = boto3.client('s3')
    rekognition = boto3.client('rekognition')

    key = event['image_key']
    parking_space_id = event['parking_space_id']

    obj = s3.get_object(Bucket=bucket, Key=key)
    image = obj['Body'].read()

    response = rekognition.detect_labels(Image={'Bytes': image})

    fire = False
    car = False

    labels = []
    for label in response['Labels']:
        name = label['Name'].lower()

        if label['Confidence'] > 75.0:
            for word in fire_words:
                if word in name:
                    fire = True
                    send_sms('Caution: Fire detected in parking space {}'.format(parking_space_id))
                    break

            for word in car_words:
                if word in name:
                    car = True

        labels.append({
            'Name': name,
            'Confidence': label['Confidence']
        })

    output = {
        "image_key": key,
        "parking_space_id": parking_space_id,
        "car": car,
        "fire": fire,
        "rekognition_result": labels
    }
    return output
