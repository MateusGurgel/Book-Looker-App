import ssl
import urllib.request
import gzip
import io

from models.book import Book
from scrapping.scrappers.scrapper import Scrapper
from fake_headers import Headers # type: ignore    
from bs4 import BeautifulSoup
import os

class AmazonScrapper(Scrapper):

    def __init__(self, proxy_connector: str) -> None:   
        self.proxy_connector = proxy_connector

    def start(self) -> None:
        pass

    def stop(self) -> None:
        pass

    def get_book_price_by_link(self, book: Book) -> int:

        header = Headers( # type: ignore
            os="win",
            headers=True
        ).generate()

        proxies = {
            'http': 'http://' + self.proxy_connector,
            'https': 'http://' + self.proxy_connector,
        }


        ca_cert_path = './resources/brd/certificate.crt'
        context = ssl.create_default_context(cafile=ca_cert_path)

        opener = urllib.request.build_opener(
            urllib.request.ProxyHandler(proxies),
            urllib.request.HTTPSHandler(context=context),

        )

        request = urllib.request.Request(book.link, headers=header)

        response = opener.open(request)

        content_type = response.headers.get('Content-Encoding', '').lower()

        if 'gzip' in content_type:
            buf = io.BytesIO(response.read())
            f = gzip.GzipFile(fileobj=buf)
            response_text = f.read().decode('utf-8')
        else:
            response_text = response.read().decode('utf-8')

        try:
            soup = BeautifulSoup(response_text, 'html.parser')

            price_span = soup.select_one('span.priceToPay')

            if price_span is None:
                raise ValueError("Price span not found")

            price = price_span.select_one('span.a-price-whole')

            if price is None:
                raise ValueError("Price not found")
            
            price = price.text.replace(",", "")
            return int(price)

        except Exception as e:
            html_source = response_text
            
            os.makedirs("./logs/", exist_ok=True)

            with open("./logs/" + book.name + "_log.html", "w", encoding="utf-8") as file:
                file.write(html_source)

            raise ValueError(f"Error getting price: {e}")