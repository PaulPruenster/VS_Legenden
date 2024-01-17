import boto3

"""
 example request body:
{
    "image_key": "fire.jpeg",
    "parking_space_id": 10
}
"""


textract = boto3.client('textract')
bucket = 'verteiltesystemeparkingsystem'
fire_words = ['fire', 'flames']
car_words = ['car', "license plate", "vehicle", "transportation"]


def lambda_handler(event, context):
    key = event['image_key']

    image_object = textract.detect_document_text(
        Document={'S3Object': {'Bucket': bucket, 'Name': key}})
    text = ""
    for block in image_object['Blocks']:
        if block['BlockType'] == 'LINE':
            text += f"_{block['Text'].replace(' ', '').lower()}"

    output = {
        "image_key": key,
        "parking_space_id": event['parking_space_id'],
        "license_plate": text,
        "is_empty": text == ""
    }
    return output
