import os
import sys

sys.path.append('/home/carlos/workspace/musicbrainz/musicbrainz/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'musicbrainz.settings'
import django

django.setup()
from musicbrainz.lab.models import Artist

import json
from uuid import UUID


class UUIDEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, UUID):
            # if the obj is uuid, we simply return the value of uuid
            # return obj.hex
            return str(obj)
        return json.JSONEncoder.default(self, obj)


artists = Artist.objects.filter(type=1).values('id', 'gid', 'name')[:10]
tits = []

for i in artists:
    tits.append(i)

with open('titulares.json', 'w', encoding='utf-8') as f:
    json.dump(tits, f, cls=UUIDEncoder, ensure_ascii=False, indent=4)

print('*' * 50)
print(artists.count())
print('*' * 50)
