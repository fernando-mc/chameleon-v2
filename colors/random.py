import json
import os

from todos import decimalencoder
import boto3
dynamodb = boto3.resource('dynamodb')


def random(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    # fetch all todos from the database
    result = table.scan(
        Limit=1
    )

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Items'])
    }

    return response