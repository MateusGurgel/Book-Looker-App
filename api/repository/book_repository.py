
from typing import List
from database import get_db_cursor
from models.book import Book

class BookRepository():
    @staticmethod
    def get_all_books() -> List[Book]:
        with get_db_cursor() as cursor:
            cursor.execute("SELECT * FROM books")
            rows = cursor.fetchall()
            columns = [col[0] for col in cursor.description]
            book_dicts = [dict(zip(columns, row)) for row in rows]
            books = [Book(**book_dict) for book_dict in book_dicts]

            return books
    
    @staticmethod
    def create_book(name: str, link: str) -> None:
        with get_db_cursor() as cursor:
            cursor.execute("INSERT INTO books (name, link) VALUES (%s, %s)", (name, link))