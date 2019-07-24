import datetime
from typing import Iterator, Dict, Any
from urllib.parse import urlencode
import requests
import psycopg2
from decouple import config
import time
from functools import wraps
from memory_profiler import memory_usage


def parse_first_brewed(text: str) -> datetime.date:
    parts = text.split('/')
    if len(parts) == 2:
        return datetime.date(int(parts[1]), int(parts[0]), 1)
    elif len(parts) == 1:
        return datetime.date(int(parts[0]), 1, 1)
    else:
        assert False, ('Formato de data desconhecio', text)


def iter_beers_from_api(page_size: int = 5) -> Iterator[Dict[str, Any]]:
    session = requests.Session()
    page = 1

    while True:
        response = session.get('https://api.punkapi.com/v2/beers?' + urlencode({
            'page': page,
            'per_page': page_size
        }))
        response.raise_for_status()
        data = response.json()
        if not data:
            break

        yield from data  # AINDA NÂO SAQUEI ESSE TAL DE YIELD

        page += 1


# beers = iter_beers_from_api()


def connect():
    connection = psycopg2.connect(
        host=config('HOST_AWS'),
        database="testload",
        user=config('USER_AWS'),
        password=config('PASSWORD_AWS')
    )
    connection.autocommit = True

    return connection


def create_staging_table(cursor):
    cursor.execute("""
        DROP TABLE IF EXISTS staging_beers;
        CREATE UNLOGGED TABLE staging_beers(
          id                  INTEGER,
            name                TEXT,
            tagline             TEXT,
            first_brewed        DATE,
            description         TEXT,
            image_url           TEXT,
            abv                 DECIMAL,
            ibu                 DECIMAL,
            target_fg           DECIMAL,
            target_og           DECIMAL,
            ebc                 DECIMAL,
            srm                 DECIMAL,
            ph                  DECIMAL,
            attenuation_level   DECIMAL,
            brewers_tips        TEXT,
            contributed_by      TEXT,
            volume              INTEGER
        );
    """)


# conn = connect()
# with conn.cursor() as cursor:
#     create_staging_table(cursor)

def profile(fn):
    @wraps(fn)
    def inner(*args, **kwargs):
        fn_kwargs_str = ', '.join(f'{k}={v}' for k, v in kwargs.items())
        print(f'\n{fn.__name__}({fn_kwargs_str})')

        # Measure time
        t = time.perf_counter()
        retval = fn(*args, **kwargs)
        elapsed = time.perf_counter() - t
        print(f'Time   {elapsed:0.4}')

        # Measure memory
        mem, retval = memory_usage((fn, args, kwargs), retval=True, timeout=200, interval=1e-7)

        print(f'Memory {max(mem) - min(mem)}')
        return retval

    return inner


beers = list(iter_beers_from_api()) * 100


# len(beers)

# @profile
# def insert_one_by_one(connection, beers: Iterator[Dict[str, Any]]) -> None:
#     with connection.cursor() as cursor:
#         create_staging_table(cursor)
#         for beer in beers:
#             cursor.execute("""
#                 INSERT INTO staging_beers VALUES (
#                     %(id)s,
#                     %(name)s,
#                     %(tagline)s,
#                     %(first_brewed)s,
#                     %(description)s,
#                     %(image_url)s,
#                     %(abv)s,
#                     %(ibu)s,
#                     %(target_fg)s,
#                     %(target_og)s,
#                     %(ebc)s,
#                     %(srm)s,
#                     %(ph)s,
#                     %(attenuation_level)s,
#                     %(brewers_tips)s,
#                     %(contributed_by)s,
#                     %(volume)s
#                 );
#             """, {
#                 **beer,
#                 'first_brewed': parse_first_brewed(beer['first_brewed']),
#                 'volume': beer['volume']['value'],
#             })


# In[17]:


# print(connect())
# insert_one_by_one(connect(), beers)
# insert_one_by_one

# for beer in beers:
#     print(beer['volume']['value'])


# In[18]:


# import psycopg2.extras
#
#
# @profile
# def insert_execute_batch(connection, beers: Iterator[Dict[str, Any]]) -> None:
#     with connection.cursor() as cursor:
#         create_staging_table(cursor)
#
#         all_beers = [{
#             **beer,
#             'first_brewed': parse_first_brewed(beer['first_brewed']),
#             'volume': beer['volume']['value'],
#         } for beer in beers]
#
#         psycopg2.extras.execute_batch(cursor, """
#             INSERT INTO staging_beers VALUES (
#                 %(id)s,
#                 %(name)s,
#                 %(tagline)s,
#                 %(first_brewed)s,
#                 %(description)s,
#                 %(image_url)s,
#                 %(abv)s,
#                 %(ibu)s,
#                 %(target_fg)s,
#                 %(target_og)s,
#                 %(ebc)s,
#                 %(srm)s,
#                 %(ph)s,
#                 %(attenuation_level)s,
#                 %(brewers_tips)s,
#                 %(contributed_by)s,
#                 %(volume)s
#             );
#         """, all_beers)
#
# insert_execute_batch(connect(), beers)


# insert_execute_batch()

# In[44]:
#
# @profile
# def insert_execute_batch_iterator(connection, beers: Iterator[Dict[str, Any]]) -> None:
#     with connection.cursor() as cursor:
#         create_staging_table(cursor)
#
#         iter_beers = ({
#             **beer,
#             'first_brewed': parse_first_brewed(beer['first_brewed']),
#             'volume': beer['volume']['value'],
#         } for beer in beers)
#
#         psycopg2.extras.execute_batch(cursor, """
#             INSERT INTO staging_beers VALUES (
#                 %(id)s,
#                 %(name)s,
#                 %(tagline)s,
#                 %(first_brewed)s,
#                 %(description)s,
#                 %(image_url)s,
#                 %(abv)s,
#                 %(ibu)s,
#                 %(target_fg)s,
#                 %(target_og)s,
#                 %(ebc)s,
#                 %(srm)s,
#                 %(ph)s,
#                 %(attenuation_level)s,
#                 %(brewers_tips)s,
#                 %(contributed_by)s,
#                 %(volume)s
#             );
#         """, iter_beers)


@profile
def insert_execute_batch_iterator(
        connection,
        beers: Iterator[Dict[str, Any]],
        page_size: int = 100, ) -> None:
    with connection.cursor() as cursor:
        create_staging_table(cursor)

        iter_beers = ({
            **beer,
            'first_brewed': parse_first_brewed(beer['first_brewed']),
            'volume': beer['volume']['value'],
        } for beer in beers)

        psycopg2.extras.execute_batch(cursor, """
            INSERT INTO staging_beers VALUES (
                %(id)s,
                %(name)s,
                %(tagline)s,
                %(first_brewed)s,
                %(description)s,
                %(image_url)s,
                %(abv)s,
                %(ibu)s,
                %(target_fg)s,
                %(target_og)s,
                %(ebc)s,
                %(srm)s,
                %(ph)s,
                %(attenuation_level)s,
                %(brewers_tips)s,
                %(contributed_by)s,
                %(volume)s
            );
        """, iter_beers, page_size=page_size)


import io
from typing import Iterator, Optional


def clean_csv_value(value: Optional[Any]) -> str:
    if value is None:
        return r'\N'
    return str(value).replace('\n', '\\n')


@profile
def copy_stringio(connection, beers: Iterator[Dict[str, Any]]) -> None:
    with connection.cursor() as cursor:
        create_staging_table(cursor)
        csv_file_like_object = io.StringIO()
        for beer in beers:
            csv_file_like_object.write('|'.join(map(clean_csv_value, (
                beer['id'],
                beer['name'],
                beer['tagline'],
                parse_first_brewed(beer['first_brewed']),
                beer['description'],
                beer['image_url'],
                beer['abv'],
                beer['ibu'],
                beer['target_fg'],
                beer['target_og'],
                beer['ebc'],
                beer['srm'],
                beer['ph'],
                beer['attenuation_level'],
                beer['contributed_by'],
                beer['brewers_tips'],
                beer['volume']['value'],
            ))) + '\n')
        csv_file_like_object.seek(0)
        cursor.copy_from(csv_file_like_object, 'staging_beers', sep='|')


# conn = connect()
# insert_execute_batch_iterator(conn, iter(beers), page_size=1000)
from typing import Iterator, Optional
import io


class StringIteratorIO(io.TextIOBase):
    def __init__(self, iter: Iterator[str]):
        self._iter = iter
        self._buff = ''

    def readable(self) -> bool:
        return True

    def _read1(self, n: Optional[int] = None) -> str:
        while not self._buff:
            try:
                self._buff = next(self._iter)
            except StopIteration:
                break
        ret = self._buff[:n]
        self._buff = self._buff[len(ret):]
        return ret

    def read(self, n: Optional[int] = None) -> str:
        line = []
        if n is None or n < 0:
            while True:
                m = self._read1()
                if not m:
                    break
                line.append(m)
        else:
            while n > 0:
                m = self._read1(n)
                if not m:
                    break
                n -= len(m)
                line.append(m)
        return ''.join(line)


@profile
def copy_string_iterator(connection, beers: Iterator[Dict[str, Any]]) -> None:
    with connection.cursor() as cursor:
        create_staging_table(cursor)
        beers_string_iterator = StringIteratorIO((
            '|'.join(map(clean_csv_value, (
                beer['id'],
                beer['name'],
                beer['tagline'],
                parse_first_brewed(beer['first_brewed']).isoformat(),
                beer['description'],
                beer['image_url'],
                beer['abv'],
                beer['ibu'],
                beer['target_fg'],
                beer['target_og'],
                beer['ebc'],
                beer['srm'],
                beer['ph'],
                beer['attenuation_level'],
                beer['brewers_tips'],
                beer['contributed_by'],
                beer['volume']['value'],
            ))) + '\n'
            for beer in beers
        ))
        cursor.copy_from(beers_string_iterator, 'beers', sep='|')


if __name__ == '__main__':
    conn = connect()
    insert_execute_batch_iterator(conn, beers, page_size=1000)
