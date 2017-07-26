import json
import os

from colorthief import ColorThief

PICTURES_DIR = 'pictures'

for filename in os.listdir(PICTURES_DIR):
    color_thief = ColorThief('./pictures/' + filename)
    dominant_color = color_thief.get_color(quality=1)
    palette = color_thief.get_palette(color_count=6)
    result = {
        "rgb": {
            "dominant": dominant_color,
            "palette": palette
        }
    }
    print dominant_color
    print palette
    json.dumps(result)
    

# Format to use for table data
# { "rgb": 
#     {
#         "dominant": "(232, 240, 229)",
#         "palette": [
#             "(103, 119, 45)", 
#             "(50, 88, 57)",
#             "(237, 244, 238)", 
#             "(119, 156, 121)",
#             "(80, 119, 94)", 
#             "(173, 190, 128)"
#         ]
#     }
# }

# { "rgb": 
#     {
#         "dominant": "(60, 46, 29)",
#         "palette": [
#             "(58, 44, 26)", 
#             "(216, 170, 121)",
#             "(170, 87, 15)", 
#             "(170, 182, 191)",
#             "(89, 122, 157)", 
#             "(115, 113, 98)"
#         ]
#     }
# }


# { "rgb": 
#     {
#         "dominant": "(60, 46, 29)",
#         "palette": [
#             "(58, 44, 26)", 
#             "(216, 170, 121)",
#             "(170, 87, 15)", 
#             "(170, 182, 191)",
#             "(89, 122, 157)", 
#             "(115, 113, 98)"
#         ]
#     }
# }
