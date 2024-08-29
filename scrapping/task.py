from datetime import datetime

from scrapping.scrappers.amazon_scrapper import AmazonScrapper
from services.book_log_service import BookLogService
from services.books_service import BookService

def log_books():

    scrapper = AmazonScrapper()
    scrapper.start()

    books = BookService.get_all_books()

    if books:
        for book in books:
            price = scrapper.get_product_price_by_link(book.link)
            date = datetime.today().date()

            BookLogService.create_book_log(price, date, book.id)

    scrapper.stop()