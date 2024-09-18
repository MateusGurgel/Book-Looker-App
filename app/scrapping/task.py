from datetime import datetime

from scrapping.scrappers.amazon_scrapper import AmazonScrapper
from services.book_log_service import BookLogService
from services.books_service import BookService

import logging

logger = logging.getLogger(__name__)

def log_books():
    logger.info("Starting to log books")

    scrapper = AmazonScrapper()
    scrapper.start()

    books = BookService.get_all_books()

    if books:
        for book in books:
            
            logger.info(f"Getting price for book: {book.name}")

            try:
                price = scrapper.get_book_price_by_link(book)
            except ValueError as e:
                logger.error(f"Error getting price for book: {book.name}")
                logger.error(e)
                continue
            
            date = datetime.today().date()

            BookLogService.create_book_log(price, date, book.id)

    scrapper.stop()