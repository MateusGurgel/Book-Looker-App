from models.book import Book
from scrapping.scrappers.scrapper import Scrapper

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

class AmazonScrapper(Scrapper):

    def __init__(self) -> None:
        self.driver = None

    def start(self) -> None:
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        options.add_argument('--window-size=1920x1080')

        driver = webdriver.Chrome(options=options)

        self.driver = driver

    def stop(self) -> None:
        self.driver.quit()

    def get_book_price_by_link(self, book: Book) -> int:
        driver = self.driver


        try:
            driver.get(book.link)
            price_element = driver.find_element(By.CLASS_NAME, "a-price-whole")
        except NoSuchElementException as e:

            html_source = driver.page_source
            with open("./logs/" + book.name + "_log.html", "w", encoding="utf-8") as file:
                file.write(html_source)

            raise ValueError(f"Error getting price: {e}")
            

        price = int(price_element.text)

        return price
