import json
import logging
import os
import time
import uuid

import boto3
dynamodb = boto3.resource('dynamodb')


def create(event, context):
    data = json.loads(event['body'])
    if 'rgb' not in data:
        logging.error("Validation Failed")
        raise Exception("Couldn't create the color item.")
        return

    timestamp = int(time.time() * 1000)

    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    item = {
        'id': str(uuid.uuid1()),
        'rgb': data['rgb'],
        'createdAt': timestamp,
    }

    # Write the color to the database
    table.put_item(Item=item)

    # Create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(item)
    }

    return response