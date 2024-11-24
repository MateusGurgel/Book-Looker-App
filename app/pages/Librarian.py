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

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {
                "role": "Librarian",
                "content": "Olá! Você precisa de alguma recomendação de livros? Veio ao lugar certo! 👋"
            }
        ]

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    prompt = st.chat_input("O que você procura?")

    if prompt:
        
        with st.chat_message("You"):
            st.write(prompt)

        st.session_state.messages.append({"role": "user", "content": prompt})
        
        with st.spinner("Esperando resposta do Bibliotecário..."):
            st.session_state.messages.append({"role": "Librarian", "content": get_librarian_response(prompt)})
            st.rerun()

if __name__ == "__main__":
    main()