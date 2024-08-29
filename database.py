import psycopg2

from decouple import config

from contextlib import contextmanager

@contextmanager
def get_db_cursor():

    conn = psycopg2.connect(
    dbname=config("DATABASE_NAME"),
    user=config("DATABASE_USER"),
    password=config("DATABASE_PASSWORD"),
    host=config("DATABASE_HOST"),
    port=config("DATABASE_PORT")
    )

    cursor = conn.cursor()
    try:
        yield cursor
    finally:
        conn.commit()
        conn.close()