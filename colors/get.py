import os
import json

from todos import decimalencoder
import boto3
dynamodb = boto3.resource('dynamodb')


def get(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    # Fetch color from the database
    result = table.get_item(
        Key={
            'id': event['pathParameters']['id']
        }
    )

    # Create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Item'])
    }

    return response