from typing import List
from models.book_log import BookLog
import streamlit as st
import pandas as pd
import requests
from env import API_LINK

@st.cache_data(ttl=3600)
def get_book_logs(book_id: int) -> List[BookLog]:

    response = requests.get(API_LINK + f"/books/{book_id}/logs")
    response = response.json()
    book_logs = [BookLog(**log) for log in response]

    return book_logs

def print_book_logs(book_id: int) -> None:
    logs: List[BookLog] = get_book_logs(book_id)

    if not logs:
        st.markdown(f"Não há logs para o livro escolhido")
        return

    log_dicts = [log.__dict__ for log in logs]
    logs_dataset = pd.DataFrame(log_dicts)
    logs_dataset = logs_dataset.drop(["id", "book_id"], axis=1)

    price_mean = logs_dataset["price"].mean()
    recent_price = logs_dataset.sort_values("date").iloc[0]["price"]

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Média de preços", price_mean)

    with col2:
        st.metric("Econimia comprando agora", recent_price - price_mean)

    with col3:
        state = "Comprar" if price_mean < recent_price else "Aguardar"
        st.markdown(f"### Está na hora de: **{state}**")

    st.line_chart(logs_dataset, y="price", x="date", x_label="Data", y_label="Preço (R$)")
