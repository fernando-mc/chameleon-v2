import boto3
import json
import os

from colors import decimalencoder

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
        "body": json.dumps(
            result['Item'], 
            cls=decimalencoder.DecimalEncoder
        )
    }

    return response