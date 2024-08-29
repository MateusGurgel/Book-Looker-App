from scrapping.scrappers.scrapper import Scrapper

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver

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

    def get_product_price_by_link(self, url: str) -> int:
        driver = self.driver

        driver.get(url)

        price_element = driver.find_element(By.CLASS_NAME, "a-price-whole")
        price = int(price_element.text)

        return price
