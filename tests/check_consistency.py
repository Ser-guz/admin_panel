import sqlite3

import psycopg2
from psycopg2.extras import DictCursor

from sqlite_to_postgres import load_data, select_film_work, pg_select_film_work


# import os
# import dotenv

# dotenv.load_dotenv('.env')

def test_amount_records():
    """Проверяет целостность данных, сравнивая число записей в обоих БД"""

    # TODO Сделать фикстуру
    dsl = {
        'dbname': 'movies_database',
        'user': 'app',
        'password': '123qwe',
        'host': '127.0.0.1',
        'port': 5432,
    }

    # TODO для подключения к базам сделать фикстуру
    with sqlite3.connect('/home/sguzun/Projects/yandex_practicum/admin_panel/sqlite_to_postgres/db.sqlite') as sqlite_conn, psycopg2.connect(
            **dsl, cursor_factory=DictCursor) as pg_conn:
        sqlite_cursor = sqlite_conn.cursor()
        pg_cursor = pg_conn.cursor()

        amount_records_1 = load_data.amount_records_in_table(sqlite_cursor, 'film_work', 'main')
        amount_records_2 = load_data.amount_records_in_table(pg_cursor, 'film_work', 'content')
        assert amount_records_1 == amount_records_2

        amount_records_3 = load_data.amount_records_in_table(sqlite_cursor, 'genre_film_work', 'main')
        amount_records_4 = load_data.amount_records_in_table(pg_cursor, 'genre_film_work', 'content')
        assert amount_records_3 == amount_records_4

        amount_records_5 = load_data.amount_records_in_table(sqlite_cursor, 'genre', 'main')
        amount_records_6 = load_data.amount_records_in_table(pg_cursor, 'genre', 'content')
        assert amount_records_5 == amount_records_6

        amount_records_7 = load_data.amount_records_in_table(sqlite_cursor, 'person_film_work', 'main')
        amount_records_8 = load_data.amount_records_in_table(pg_cursor, 'person_film_work', 'content')
        assert amount_records_7 == amount_records_8

        amount_records_9 = load_data.amount_records_in_table(sqlite_cursor, 'person', 'main')
        amount_records_10 = load_data.amount_records_in_table(pg_cursor, 'person', 'content')
        assert amount_records_9 == amount_records_10


    # assert amount_records_1 == amount_records_2


def test_content_records():
    """Проверяет корректность переноса данных, сравнивая содержимое записей в обоих БД"""

    # TODO Сделать фикстуру
    dsl = {
        'dbname': 'movies_database',
        'user': 'app',
        'password': '123qwe',
        'host': '127.0.0.1',
        'port': 5432,
    }

    # TODO для подключения к базам сделать фикстуру
    with sqlite3.connect('/home/sguzun/Projects/yandex_practicum/admin_panel/sqlite_to_postgres/db.sqlite') as sqlite_conn, psycopg2.connect(
            **dsl, cursor_factory=DictCursor) as pg_conn:
        sqlite_cursor = sqlite_conn.cursor()
        pg_cursor = pg_conn.cursor()

        # Сделать выборку данных из таблиц разных БД
        # Сравнить

        select_film_work = """SELECT 
                            id, 
                            title, 
                            description,
                            rating, 
                            "type"
                        FROM main.film_work"""
        film_works_1 = sqlite_cursor.execute(select_film_work).fetchone()[0]
        film_works_1 = [item for item in film_works_1]

        pg_select_film_work = """SELECT
                               id, 
                               title,
                               description,
                               rating,
                               "type"
                           FROM content.film_work"""
        pg_cursor.execute(pg_select_film_work)
        film_works_2 = pg_cursor.fetchone()[0]
        film_works_2 = [item for item in film_works_2]
        assert film_works_1 == film_works_2