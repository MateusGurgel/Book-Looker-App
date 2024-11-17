import logging
from typing import List
from urllib import response
from models.book import Book
from models.book_log import BookLog
import streamlit as st
import pandas as pd
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

    print(response)

    response = response.json()
    
    book_list = [Book(**book) for book in response]

    return book_list

@st.cache_data(ttl=3600)
def get_book_logs(book_id: int) -> List[BookLog]:

    response = requests.get(API_LINK + f"/books/{book_id}/logs")
    response = response.json()
    book_logs = [BookLog(**log) for log in response]

    return book_logs

def print_book_logs(book_id: int, book_name: str) -> None:
    logs: List[BookLog] = get_book_logs(book_id)

    if not logs:
        st.markdown(f"Não há logs para o livro: {book_name}")
        return
    
    log_dicts = [log.__dict__ for log in logs]
    logs_dataset = pd.DataFrame(log_dicts)
    logs_dataset = logs_dataset.drop(["id", "book_id"], axis=1)

    st.markdown(f"## Logs do livro: {book_name}")
    st.title("Preço x Tempo")
    st.line_chart(logs_dataset, y="price", x="date", x_label="Data", y_label="Preço (R$)")
    st.download_button("Baixar logs", logs_dataset.to_csv(), "logs.csv")

def main():
    st.title("Book Looker")

    books = get_books()

    id_to_name = {str(book.id) + " - " + book.name: book.id for book in books}

    selected_book_name = st.selectbox("Selecione uma opção", list(id_to_name.keys()))

    selected_book_id = id_to_name[selected_book_name]

    print_book_logs(selected_book_id, selected_book_name)

if __name__ == "__main__":
    main()