
import requests
from bs4 import BeautifulSoup as bs

page_address = 'https://wallpaperlist.com'
page_source = requests.get(page_address).content

# print(page_source)

parser = bs(page_source, 'html.parser')
images = parser.find_all('img')

for image in images:
    image_address = page_address + image['src']
    # print(image_address)
    image_data = requests.get(image_address).content
