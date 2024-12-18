import logging
from services.books_service import BookService
from services.book_log_service import BookLogService
from fastapi import FastAPI
from services.librarian_service import LibrarianService
from pydantic import BaseModel

logging.basicConfig(level=logging.INFO)

app = FastAPI()

@app.get("/books")
def read_root():
    return BookService.get_all_books()

class LibrarianQuestion(BaseModel):
    past_interactions: str
    question: str

class LibrarianResponse(BaseModel):
    response: str

@app.post("/librarian")
def generate_response(question: LibrarianQuestion) -> LibrarianResponse:
    return {"response": LibrarianService.generate_response(question.past_interactions, question.question)}

@app.get("/books/{book_id}/logs")
def read_item(book_id: int):
    return BookLogService.get_book_logs_by_id(book_id)
