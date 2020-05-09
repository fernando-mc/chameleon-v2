import boto3
import json
import os
import uuid

s3 = boto3.client('s3')


def generate_presigned_url():
    object_name = str(uuid.uuid4())
    response = s3.generate_presigned_post(
        'chameleon-photos',
        object_name,
        Fields={
            "acl": "public-read",
            "content-length-range": [0, 1000000]
        },
        Conditions=[
            {"acl": "public-read"},
            ["content-length-range", 0, 1000000]
        ],
        ExpiresIn=3600
    )
    response = response["fields"]
    del response["content-length-range"]
    return response


def handler(event, context):
    url_details = generate_presigned_url()
    response = {
        "statusCode": 200,
        "headers": {"Access-Control-Allow-Origin": "*"},
        "body": json.dumps(url_details)
    }
    return response
