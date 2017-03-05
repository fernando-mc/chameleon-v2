import requests
import re
import time
import json


url_regex = r"<div class=\"nav-previous\"><a href=\"[A-Za-z:/.\-0-9]*"

h5_color_regex = r"<h5>#[0-9A-Z]{6}"

title_regex = r"entry-title\">{[A-Za-z ]*}"

FIRST_URL = "https://www.design-seeds.com/studio-hues/collage/color-collect-3/"
page_url_to_search = FIRST_URL

blog_urls = []
color_options = {}

x = 0

while x < 500:
    time.sleep(5)
    x += 1
    # Get new page text
    new_page_text = requests.get(page_url_to_search).text
    # Regex search for matches on title, url and hex value
    re_new_title_name = re.finditer(title_regex, new_page_text)
    re_new_url = re.finditer(url_regex, new_page_text)
    re_new_hexes = re.finditer(h5_color_regex, new_page_text)
    # get the actual values for the above and add to lists/dicts
    for match in re_new_title_name:
        title = match.group()[14:-1]
        print(title)
        break
    hex_array = []
    for hexes in re_new_hexes:
        single_hex = hexes.group()[4:]
        hex_array.append(single_hex)
        print(hex_array)
    color_options.update({title:hex_array})
    print(color_options)
    for urls in re_new_url:
        url = urls.group()[35:]
        blog_urls.append(url)
        break
    page_url_to_search = url
    print(page_url_to_search)