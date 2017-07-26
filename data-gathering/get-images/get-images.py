import requests
import shutil
import time
from bs4 import BeautifulSoup

BASE_URL = 'https://www.pexels.com/search/landscape/?page={0}'

def get_images_urls_from_page(url):
    main_page = requests.get(url)
    soup = BeautifulSoup(main_page.text, 'html.parser')
    images = soup.findAll('img')
    time.sleep(1)  # Never spam a page with requests
    validated_images = []
    for i in images:
        try:
            if i['src'][0:5] == 'https':
                validated_images.append(i)
        except Exception:
            pass
    return validated_images

def download_image_urls(url_array, file_prefix):
    count = 1
    for i in url_array:
        response = requests.get(i['src'], stream=True)
        time.sleep(1) # wait in between downloading images - avoiding spaming page
        with open('{0}_{1}.png'.format(file_prefix,str(count)), 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        del response
        count += 1

i = 1
while i < 20:
    url_array = get_images_urls_from_page(BASE_URL.format(str(i)))
    download_image_urls(url_array, 'page_' + str(i))
    i += 1
