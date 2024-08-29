from typing import List
from models.book import Book

from repository.book_repository import BookRepository
class BookService():
    @staticmethod
    def get_all_books() -> List[Book]:
        return BookRepository.get_all_books()
    
    @staticmethod
    def create_book(name: str, link: str) -> None:
        BookRepository.create_book(name, link)