from abc import ABC, abstractmethod

class Scrapper(ABC):
    @abstractmethod
    def get_product_price_by_link(self, url) -> int:
        pass