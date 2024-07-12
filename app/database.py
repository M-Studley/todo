import psycopg2
from psycopg2.extras import RealDictCursor
from .config import Config


class Database:
    conn: psycopg2.extensions.connection = None
    curs: RealDictCursor = None

    @classmethod
    def init(cls):
        Database.conn = psycopg2.connect(Config.DATABASE_URL)
        Database.curs = Database.conn.cursor(cursor_factory=RealDictCursor)

    @classmethod
    def fetchall(cls, query: str) -> list[dict]:
        Database.curs.execute(query)
        print(f"Running {query}")
        return Database.curs.fetchall()

    @classmethod
    def fetchone(cls, query: str) -> dict:
        Database.curs.execute(query)
        print(f"Running {query}")
        return Database.curs.fetchone()

    @classmethod
    def executemany(cls, query: str, data: list[tuple]) -> None:
        print("Executing many...")
        Database.curs.executemany(query, data)
        Database.conn.commit()

    @classmethod
    def execute(cls, query: str, data: tuple = ()) -> None:
        print("Executing one...")
        Database.curs.execute(query, data)
        Database.conn.commit()


if not Database.conn:
    Database.init()
