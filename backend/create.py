import boto3
import json
import logging
import os
import time

from backend import generate_schemes
from colorthief import ColorThief

generate_color_scheme = generate_schemes.generate_color_scheme

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])
s3 = boto3.resource('s3')


def create(event, context):
    s3_key = event['Records'][0]['s3']['object']['key']
    local_file_name = '/tmp/' + s3_key
    s3.Bucket('chameleon-photos').download_file(s3_key, local_file_name)
    color_scheme = generate_color_scheme(local_file_name)
    # Remove the object from tmp space
    if os.path.exists(local_file_name):
        os.remove(local_file_name)
    item = {
        'pk': s3_key,
        'rgb': color_scheme,
    }
    # Write the color to the database
    table.put_item(Item=item)
    # Create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(item)
    }
    return response
