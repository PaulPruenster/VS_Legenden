def lambda_handler(event, context):
    return {
        'parking_space_id': event['parking_space_id'],
        'is_empty': True,
        'license_plate': ''
    }
