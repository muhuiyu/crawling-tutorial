from bs4 import BeautifulSoup
import json, requests, os
import urllib.request
from urllib import error

url = input('Enter a LINE sticker website to extract\n> ')
r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')
title = soup.find("p", class_='mdCMN38Item01Ttl').text

if not os.path.isdir(title): os.mkdir(title)

# Cover Image
cover_data = json.loads(soup.find('div', attrs={'class': 'mdCMN38Img'})['data-preview'])
cover_name = title+'/main_'+cover_data['id']+'.png'
cover_url = cover_data['staticUrl'].split(';')[0]

try:
    urllib.request.urlretrieve(cover_url, cover_name)
    print(cover_name)
except error.URLError as e:
    print(e.reason)

# Stickers

sticker_data_list = []
raw_sticker_list = soup.find_all('li', attrs={'class': 'mdCMN09Li'})    # class_='mdCMN09Li'
for raw in raw_sticker_list:
    sticker_data_list.append(json.loads(raw['data-preview']))

for sticker_data in sticker_data_list:
    sticker_url = sticker_data['staticUrl'].split(';')[0]
    sticker_name = title+'/sticker_'+sticker_data['id']+'.png'

    try:
        urllib.request.urlretrieve(sticker_url, sticker_name)
        print(sticker_name)
    except error.URLError as e:
        print(e.reason)
