from sqlite3 import Date


class BookLog:
    def __init__(self, id: int, price: int, date: Date, book_id: int):
        self.id = id
        self.price = price
        self.date = date
        self.book_id = book_id

