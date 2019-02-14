import json
from time import time
from time import sleep
from random import randint
from requests import get
from bs4 import BeautifulSoup
import pandas as pd

with open('titulares.json', 'r') as f:
    tits = json.load(f)

url = 'https://musicbrainz.org/artist/'
# url = 'https://musicbrainz.org/artist/42a636a0-dbe4-4d0c-abe2-1590fad9531b/works'
for gid in tits[:10]:
    link = str(url + gid['gid'] + '/works')

    # Pause the loop
    sleep(randint(8, 15))

    response = get(link)
    # html_soup = BeautifulSoup(response.text, 'html.parser')
    html_soup = BeautifulSoup(response.content, 'lxml')

    table = html_soup.find('table', class_='tbl')
    if table:
        mygid = gid['gid']
        ds = pd.read_html(link)
        ds[0]['gid'] = mygid
        namefile = str('files/' + mygid + '.json')
        # ds[0].to_json(namefile, orient='table')

        # with open('obras4.json', 'a', encoding='utf-8') as f:
        with open(namefile, 'w', encoding='utf-8') as f:
            f.write(ds[0].to_json(orient='records', force_ascii=False))

            print('*' * 50)
            print(link)
            print('*' * 50)
