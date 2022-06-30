import logging
import sqlite3
from dataclasses import dataclass
from typing import List, Tuple

import psycopg2
from psycopg2.extensions import connection as _connection
from psycopg2.extras import DictCursor

from sqlite_to_postgres.querys import *
from sqlite_to_postgres import settings


logger = logging.getLogger(__name__)

def amount_records_in_table(cursor, name_table: str, schema: str) -> int:
    """Вычисляет количество записей в таблице."""

    query_count = 'SELECT count(*) from {}.{}'.format(schema, name_table)
    cursor.execute(query_count)
    amount_records = cursor.fetchall()[0][0]
    return amount_records


@dataclass
class SQLiteLoader:
    """Выгрузка и обработка данных из sqlite-DB."""

    connection: sqlite3.Connection

    def load_records(self, name_table: str, query: str) -> List[Tuple]:
        records = []
        try:
            cursor = self.connection.cursor()
            amount = amount_records_in_table(cursor, name_table, 'main')
            for loading_records in range(99, amount + 100, 100):
                records.append(cursor.execute(query).fetchmany(loading_records)[0])
            cursor.close()
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
            cursor = self.connection.cursor()
            cursor.executemany(query, data)
            self.connection.commit()
            cursor.close()
        except Exception as ex:
            logger.error(
                'При вставке данные в таблицу {} возникла непредвиденная ошибка: {}'.format(
                    name_table, ex
                )
            )


def load_records_from_table(
    loader: SQLiteLoader, saver: PostgresSaver, name_table: str, query_select, query_insert
):
    """Миграция записей одной таблицы."""

    records = loader.load_records(name_table, query_select)
    saver.save_all_data(name_table, query_insert, records)


def load_records_from_db(sqlite_conn: sqlite3.Connection, pg_conn: _connection):
    """Основной метод загрузки данных из SQLite в Postgres"""

    pg_saver = PostgresSaver(pg_conn)
    sqlite_loader = SQLiteLoader(sqlite_conn)



    load_records_from_table(
        sqlite_loader, pg_saver, 'film_work', select_film_work, insert_film_work
    )
    load_records_from_table(
        sqlite_loader, pg_saver, 'genre', select_genre, insert_genre
    )
    load_records_from_table(
        sqlite_loader,
        pg_saver,
        'genre_film_work',
        select_genre_film_work,
        insert_genre_film_work,
    )
    load_records_from_table(
        sqlite_loader, pg_saver, 'person', select_person, insert_person
    )
    load_records_from_table(
        sqlite_loader,
        pg_saver,
        'person_film_work',
        select_person_film_work,
        insert_person_film_work,
    )


if __name__ == '__main__':
    print(settings.dsl)
    with sqlite3.connect('db.sqlite') as sqlite_conn, psycopg2.connect(
        **settings.dsl, cursor_factory=DictCursor
    ) as pg_conn:
        load_records_from_db(sqlite_conn, pg_conn)
        # sqlite_conn.close()
