import streamlit as st
import numpy as np
import time
import requests
from env import API_LINK

st.set_page_config(
    page_title="Book Looker",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

def get_librarian_response(prompt: str) -> str:

    response = requests.post(API_LINK + "/librarian", json={"question": prompt})

    return response.json()["response"]

def main():
    st.title("Bibliotecario")
    with st.chat_message("Librarian"):
        st.write("Olá! Você precisa de alguma recomendação de livros? Veio ao lugar certo! 👋")    
    
    prompt = st.chat_input("Diga algo!")

    if prompt:
        with st.chat_message("You"):
            st.write(prompt)

        with st.chat_message("Librarian"):
            with st.spinner('Carregando resposta...'):
                st.write(get_librarian_response(prompt))

if __name__ == "__main__":
    main()