import boto3    
s3 = boto3.resource('s3')
bucket = s3.Bucket('chameleon-photos')


def handler(event, context):
    bucket.objects.all().delete()
    return f'success deleting all objects in {bucket}'
