import json
from colorthief import ColorThief


def generate_color_scheme(filename):
    # Loop over images and get dominant color and palette for each
    color_thief = ColorThief(filename)
    dominant_color = 'rgb' + str(color_thief.get_color(quality=1))
    palette = color_thief.get_palette(color_count=6)
    # Setup for next loop
    palette_template = ''
    result_template = '"dominant": "{0}", "palette": [{1}]'
    for color in palette:
        palette_template += (json.dumps('rgb' + str(color)) + ', ')
    full_palette = palette_template[:-2]
    result = '{' + result_template.format(dominant_color, full_palette) + '}'
    return result


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
