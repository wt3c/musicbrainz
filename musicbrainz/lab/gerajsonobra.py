import json
from requests import get
from bs4 import BeautifulSoup
import pandas as pd


with open('titulares.json', 'r') as f:
    tits = json.load(f)

# url 'https://musicbrainz.org/artist/42a636a0-dbe4-4d0c-abe2-1590fad9531b/works'
url = 'https://musicbrainz.org/artist/'

for gid in tits[:10]:
    link = str(url + gid['gid'] + '/works')
    # print(link)
    response = get(link)
    # print(response)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    # print(html_soup)

    """
            table_work class="tbl">
            <thead>
                <tr>
                    <th> Work 'Obra'</tr>
                    <th> Writers </th>
                    <th> Artists </th>
                    <th> ISWC </th>
                    <th> Type </th>
                    <th> Lyrics Languages </th>
                    <th> Attributes </th>
                    <th> Ratting </th>
                </tr>
            </thead>
            <tbody>
                <tr> -- RAW
                    <td> --COLUMN
                        <bdi> Tom Morello </bdi> -- Real Name
                    </td>
                </tr>
            </tbody>
    """
    # (lyricist, composer) ; (writer)
    # for tr in html_soup.find_all(table', class_='tbl'):


    data = pd.read_html(html_soup, header=0)
    print(data[0])

    # table_work = html_soup.find('table', {'class': 'tbl'})
    # print(table_work)


    # for wr in tr.find_all('td'):
    # print(wr)
    #     if 'writer' in str(wr):
    #         print(wr)


# table_div = html_soup.find_all(table_work', class_='tbl')
# writers = table_div.find_all('th', value_='Writers')
# print(writers)
