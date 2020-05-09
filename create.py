import boto3
import json
import logging
import os
import time

from generate_schemes import generate_color_scheme
from colorthief import ColorThief

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])
s3 = boto3.resource('s3')


def create(event, context):
    print(event)
    s3_key = event['Records'][0]['s3']['object']['key']
    local_file_name = '/tmp/' + s3_key
    s3.Bucket('chameleon-photos').download_file(s3_key, local_file_name)
    color_scheme = generate_color_scheme(local_file_name)
    print('COLOR SCHEME:')
    print(color_scheme)
    print('COLOR SCHEME ^')
    item = {
        'pk': s3_key,
        'rgb': color_scheme['rgb'],
    }
    # Write the color to the database
    table.put_item(Item=item)

    # Create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(item)
    }

    return response