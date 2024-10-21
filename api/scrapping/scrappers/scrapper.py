from abc import ABC, abstractmethod

from models.book import Book

class Scrapper(ABC):

    @abstractmethod
    def start(self) -> None:
        pass

    @abstractmethod
    def stop(self) -> None:
        pass

    @abstractmethod
    def get_book_price_by_link(self, book: Book) -> int:
        pass