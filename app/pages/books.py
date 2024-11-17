import logging
from models.book import Book
import streamlit as st
import requests
from env import API_LINK

logging.basicConfig(level=logging.INFO)

@st.cache_data(ttl=3600)
def get_books():

    response = requests.get(API_LINK + "/books")

    print(response)

    response = response.json()
    
    book_list = [Book(**book) for book in response]

    return book_list

def main():
    st.title("Book Looker")

    books = get_books()

    for book in books:
        st.markdown(f"## {book.name}")
        st.markdown(f"**Link:** {book.link}")
        st.markdown(f"---")

if __name__ == "__main__":
    main()