import sqlite3
import logging
from repository.book_log_repository import BookLogRepository
from datetime import date


logger = logging.getLogger(__name__)


class BookLogService:
    @staticmethod
    def create_book_log(price: int, date: date, book_id: int):

        try:
            BookLogRepository.create_book(price, date, book_id)
        except sqlite3.IntegrityError as error:
            logger.error(f"Erro ao criar log do livro {book_id}: {error}")

    @staticmethod
    def get_book_logs_by_id(book_id: int):
        return BookLogRepository.get_book_logs_by_id(book_id)