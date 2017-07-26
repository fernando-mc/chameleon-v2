from colorthief import ColorThief

PICTURES_DIR = 'pictures'

for filename in os.listdir(PICTURES_DIR):
    color_thief = ColorThief('./pictures/' + filename)
    dominant_color = color_thief.get_color(quality=1)
    palette = color_thief.get_palette(color_count=6)
    print dominant_color
    print palette

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