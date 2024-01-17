import boto3

s3_client = boto3.client('s3')
bucket_name = "verteiltesystemeparkingsystem"


def lambda_handler(event, context):
    key = None
    for inp in event:
        if 'image_key' in inp:
            key = inp['image_key']
            break
    if key is None:
        return {
            'message': "no image_key was found to delete"
        }
    s3_client.delete_object(Bucket=bucket_name, Key=key)
    return {
        'message': "image was removed."
    }
