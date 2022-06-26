import logging
import os
import sqlite3
from dataclasses import dataclass
from typing import List, Tuple

import dotenv
import psycopg2
from psycopg2.extensions import connection as _connection
from psycopg2.extras import DictCursor

import querys

logger = logging.getLogger(__name__)
dotenv.load_dotenv()


@dataclass
class SQLiteLoader:
    """Выгрузка и обработка данных из sqlite-DB."""

    connection: sqlite3.Connection

    def amount_records_in_table(self, name_table: str) -> int:
        """Считает количество записей в таблице."""

        cur = self.connection.cursor()
        amount = cur.execute('SELECT count(*) from main.{}'.format(name_table)).fetchall()[0]
        return amount

    def load_records(self, name_table: str, query: str) -> List[Tuple]:
        records = []
        try:
            cur = self.connection.cursor()
            amount = self.amount_records_in_table(name_table)
            for loading_records in range(99, amount + 100, 100):
                records.append(cur.execute(query).fetchmany(loading_records)[0])
        except Exception as ex:
            logger.error(
                'При чтении таблицы {} возникла непредвиденная ошибка: {}'.format(
                    name_table, ex
                )
            )
        return records


@dataclass
class PostgresSaver:
    """Вставка и сохранение строк в postgresql-DB."""

    connection: _connection

    def save_all_data(self, name_table: str, query: str, data: List[Tuple]) -> None:
        try:
            cur = self.connection.cursor()
            cur.executemany(query, data)
            self.connection.commit()
        except Exception as ex:
            logger.error(
                'При вставке данные в таблицу {} возникла непредвиденная ошибка: {}'.format(
                    name_table, ex
                )
            )


def load_from_sqlite(sqlite_conn: sqlite3.Connection, pg_conn: _connection):
    """Основной метод загрузки данных из SQLite в Postgres"""

    postgres_saver = PostgresSaver(pg_conn)
    sqlite_loader = SQLiteLoader(sqlite_conn)

    # 1 - film_work
    film_works = sqlite_loader.load_records('film_work', querys.select_film_work)
    postgres_saver.save_all_data('film_work', querys.insert_film_work, film_works)

    # 2 - genre
    genres = sqlite_loader.load_records('genre', querys.select_genre)
    postgres_saver.save_all_data('genre', querys.insert_genre, genres)

    # 3 - genre_film_work
    genre_film_works = sqlite_loader.load_records(
        'genre_film_work', querys.select_genre_film_work
    )
    postgres_saver.save_all_data(
        'genre_film_work', querys.insert_genre_film_work, genre_film_works
    )

    # 4 - person
    persons = sqlite_loader.load_records('person', querys.select_person)
    postgres_saver.save_all_data('person', querys.insert_person, persons)

    # 5 - person_film_work
    person_film_works = sqlite_loader.load_records(
        'person_film_work', querys.select_person_film_work
    )
    postgres_saver.save_all_data(
        'person_film_work', querys.insert_person_film_work, person_film_works
    )


if __name__ == '__main__':
    dsl = {
        'dbname': os.getenv('DB_NAME'),
        'user': os.getenv('USER'),
        'password': os.getenv('PASS'),
        'host': os.getenv('HOST'),
        'port': os.getenv('PORT'),
    }

    with sqlite3.connect('db.sqlite') as sqlite_conn, psycopg2.connect(
        **dsl, cursor_factory=DictCursor
    ) as pg_conn:
        load_from_sqlite(sqlite_conn, pg_conn)
        sqlite_conn.close()
