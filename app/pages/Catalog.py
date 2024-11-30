import logging
from models.book import Book
from components.book_log_ui import print_book_logs
import streamlit as st
import requests

logging.basicConfig(level=logging.INFO)

st.set_page_config(
    page_title="Book Looker",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

API_LINK = "http://localhost:8000"

@st.cache_data(ttl=3600)
def get_books():

    response = requests.get(API_LINK + "/books")

    response = response.json()
    
    book_list = [Book(**book) for book in response]

    return book_list

def main():
    st.title("Book Looker")

    books = get_books()

    id_to_name = {str(book.id) + " - " + book.name: book.id for book in books}

    selected_book_name = st.selectbox("Selecione uma opção", list(id_to_name.keys()))

    selected_book_id = id_to_name[selected_book_name]

    print_book_logs(selected_book_id)

if __name__ == "__main__":
    main()