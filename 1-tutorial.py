# Website: https://www.imdb.com/movies-in-theaters/?ref_=nv_tp_inth_1

import requests
import json
from bs4 import BeautifulSoup

# 1. Request Data
HTML_PARSER = "html.parser"
REQ_URL = 'https://www.imdb.com/movies-in-theaters/?ref_=nv_tp_inth_1'

req = requests.get(REQ_URL)
if req.status_code == requests.codes.ok:
    soup = BeautifulSoup(req.content, HTML_PARSER)
    tags = soup.find_all('td', attrs={'class': 'overview-top'})

# 2. Process Data
    data = []
    for tag in tags:
        title = tag.find('h4').get_text()                                       # title
        outline = tag.find('div', attrs={'class': 'outline'}).get_text()        # outline

        data.append({'title': title, 'outline': outline})
        print(title, outline)

# 3. Save Data
    with open('imdb.json', 'w') as file:
        json.dump(data, file)
