import os, sys
import json
from pprint import pprint
import pandas as pd

os.environ['DJANGO_SETTINGS_MODULE'] = 'musicbrainz.settings'
import django

django.setup()

from musicbrainz.lab.models import Artist, Work

file = '38697076-780a-4742-b3b2-06b79a522741.json'

with open(file, 'r')as f:
    data = f.read()
    fs = json.loads(data)

print(fs['title'])
print(fs['id'])
print(fs['attributes'])
print(fs['iswcs'])

try:
    work = Work.objects.get(gid=fs['id'])
    # print(work)

    for titular in fs['relations']:
        if not titular.get('type') == 'performance':
            # print(titular['artist']['id'], '==> ', titular['artist']['name'], '==> ', titular['type'])

            art = Artist.objects.get(gid=titular['artist']['id'])
            print(art)
            work.artists.add(art)


except Work.DoesNotExist:
    print('*' * 50)
