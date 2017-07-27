import boto3
import json
import logging
import os
import time
import uuid

from colorthief import ColorThief

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('chameleon-color-api-dev')

PICTURES_DIR = 'pictures'

for filename in os.listdir(PICTURES_DIR):
    # Loop over images and get dominant color and palette for each
    color_thief = ColorThief('./pictures/' + filename)
    dominant_color = 'rgb'+ str(color_thief.get_color(quality=1))
    palette = color_thief.get_palette(color_count=6)
    # Setup for next loop
    palette_template = ''
    result_template = '"dominant": "{0}", "palette": [{1}]'
    for color in palette:
        palette_template += (json.dumps('rgb' + str(color)) + ', ')
    full_palette = palette_template[:-2]
    result = '{' + result_template.format(dominant_color, full_palette) + '}'
    timestamp = int(time.time() * 1000)
    item = {
        'id': str(uuid.uuid1()),
        'rgb': result,
        'createdAt': timestamp,
    }
    # Write the color to the database
    table.put_item(Item=item)
    time.sleep(1)


# Format to use for table data
# {
#     "dominant": "(232, 240, 229)",
#     "palette": [
#         "(103, 119, 45)", 
#         "(50, 88, 57)",
#         "(237, 244, 238)", 
#         "(119, 156, 121)",
#         "(80, 119, 94)", 
#         "(173, 190, 128)"
#     ]
# }
 
# {
#     "dominant": "(60, 46, 29)",
#     "palette": [
#         "(58, 44, 26)", 
#         "(216, 170, 121)",
#         "(170, 87, 15)", 
#         "(170, 182, 191)",
#         "(89, 122, 157)", 
#         "(115, 113, 98)"
#     ]
# }



# 
# {
#     "dominant": "(60, 46, 29)",
#     "palette": [
#         "(58, 44, 26)", 
#         "(216, 170, 121)",
#         "(170, 87, 15)", 
#         "(170, 182, 191)",
#         "(89, 122, 157)", 
#         "(115, 113, 98)"
#     ]
# }

