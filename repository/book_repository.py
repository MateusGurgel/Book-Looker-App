
from typing import List
from database import get_db_cursor
from models.book import Book

class BookRepository():
    @staticmethod
    def get_all_books() -> List[Book]:
        with get_db_cursor() as cursor:
            cursor.execute("SELECT * FROM books")
            books = cursor.fetchall()
            books = [Book(*row) for row in books]
            return books
    
    @staticmethod
    def create_book(name: str, link: str) -> None:
        with get_db_cursor() as cursor:
            cursor.execute("INSERT INTO books (name, link) VALUES (%s, %s)", (name, link))