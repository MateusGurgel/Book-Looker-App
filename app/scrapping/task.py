from datetime import datetime

from scrapping.scrappers.amazon_scrapper import AmazonScrapper
from services.book_log_service import BookLogService
from services.books_service import BookService
from decouple import config # type: ignore
from typing import cast

import logging

logger = logging.getLogger(__name__)

PROXY_CONNECTOR = cast(str, config('BRD_PROXY_CONNECTOR', default=""))

def log_books():
    logger.info("Starting to log books")

    scrapper = AmazonScrapper(proxy_connector=PROXY_CONNECTOR)
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