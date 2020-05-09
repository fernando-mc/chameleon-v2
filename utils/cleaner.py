import boto3    
s3 = boto3.resource('s3')
bucket = s3.Bucket('chameleon-photos')


def handler(event, context):
    bucket.objects.all().delete()
    for i in range(1,7):
        key_without_folder_prefix = str(i) + '.png'
        copy_source = {
            'Bucket': 'fmc-private-assets',
            'Key': 'chameleon/' + key_without_folder_prefix
        }
        bucket.copy(copy_source, key_without_folder_prefix)
    return f'success deleting all objects in {bucket} and resetting main images.'
