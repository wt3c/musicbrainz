import os
import json
from requests import get

# url = 'http://musicbrainz.org/ws/2/work/5c0858a3-f0a3-43c9-8968-19b8d044c886?inc=artist-rels+recording-rels&fmt=json'
gid = None
with open('works.json', 'r') as f:
    works = json.load(f)

    for work in works:
        gid = work['gid']
        url = 'http://musicbrainz.org/ws/2/work/' + gid + '?inc=artist-rels+recording-rels&fmt=json'
        name_file = 'files/' + gid + '.json'
        if not os.path.exists(name_file):
            response = get(url)

            print('*' * 50)
            print('...:: BAIXANDO ::... ' + url)
            print('*' * 50)

            my_json = response.text
            tmp_json = json.dumps(my_json, ensure_ascii=False)
            wk = json.loads(tmp_json)

            with open(name_file, 'w+', encoding='utf-8') as f:
                f.write(str(wk))

            print('#' * 50)
            print('...:: SUCESSO ::... ' + url)
            print('#' * 50)
        else:
            print('O arquivo ' + gid + ' já foi baixado...')
