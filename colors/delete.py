import os

import boto3
dynamodb = boto3.resource('dynamodb')


def delete(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    # Delete the item from the database
    table.delete_item(
        Key={
            'id': event['pathParameters']['id']
        }
    )

    # Create a response
    response = {
        "statusCode": 200
    }

    return response