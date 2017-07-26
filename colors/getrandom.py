import boto3
import json
import os
import random

from colors import decimalencoder

dynamodb = boto3.resource('dynamodb')


def getrandom(event, context):
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    # fetch random item from the database
    results = table.scan()['Items']
    result = random.choice(results)

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(
            result, 
            cls=decimalencoder.DecimalEncoder
        )
    }

    return response