from typing import List
from services.books_service import BookService
from models.book_log import BookLog
import streamlit as st
from services.book_log_service import BookLogService
import pandas as pd

def print_book_logs(book_id: int, book_name: int) -> None:
    logs: List[BookLog] = BookLogService.get_book_logs_by_id(book_id)
    
    logs = [log.__dict__ for log in logs]
    logs_dataset = pd.DataFrame(logs)
    logs_dataset = logs_dataset.drop(["id", "book_id"], axis=1)

    st.markdown(f"## Logs do livro: {book_name}")
    st.write("Preço x Tempo")
    st.line_chart(logs_dataset, y="price", x="date", x_label="Data", y_label="Preço (R$)")

def main():
    st.title("Book Looker")

    books = BookService.get_all_books()

    id_to_name = {str(book.id) + " - " + book.name: book.id for book in books}

    selected_book_name = st.selectbox("Selecione uma opção", list(id_to_name.keys()))

    selected_book_id = id_to_name[selected_book_name]

    print_book_logs(selected_book_id, selected_book_name)

if __name__ == "__main__":
    main()