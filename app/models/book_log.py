from sqlite3 import Date
from pydantic import BaseModel

class BookLog(BaseModel):
    id: int
    price: int
    date: Date
    book_id: int
