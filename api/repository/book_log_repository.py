
from typing import List
from models.book_log import BookLog
from database import get_db_cursor
from datetime import date

class BookLogRepository():

    @staticmethod
    def get_book_logs_by_id(book_id: int) -> List[BookLog]:
        with get_db_cursor() as cursor:
            cursor.execute("SELECT * FROM book_logs WHERE book_id = %s", (book_id,))

            rows = cursor.fetchall()
            columns = [col[0] for col in cursor.description]
            log_dicts = [dict(zip(columns, row)) for row in rows]
            book_logs = [BookLog(**log_dict) for log_dict in log_dicts]
            return book_logs

    @staticmethod
    def create_book(price: int, date: date, book_id: int) -> None:
        with get_db_cursor() as cursor:
            cursor.execute("INSERT INTO book_logs (price, date, book_id) VALUES (%s, %s, %s)", (price, date, book_id))
