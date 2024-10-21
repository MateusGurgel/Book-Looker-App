import logging
from typing import List
from models.book import Book
from services.books_service import BookService
from models.book_log import BookLog
from services.book_log_service import BookLogService
from fastapi import FastAPI

logging.basicConfig(level=logging.INFO)

app = FastAPI()

@app.get("/books")
def read_root():
    return BookService.get_all_books()

@app.get("/books/{book_id}/logs")
def read_item(book_id: int):
    return BookLogService.get_book_logs_by_id(book_id)