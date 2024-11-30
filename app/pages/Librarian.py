import streamlit as st
import requests
from env import API_LINK
import re

from components.book_log_ui import print_book_logs

st.set_page_config(
    page_title="Book Looker",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

def get_librarian_response(past_interactions: str, prompt: str) -> str:

    response = requests.post(API_LINK + "/librarian", json={

        "past_interactions": str(past_interactions),
        "question": prompt
    })

    return response.json()["response"]

def main():
    st.title("Bibliotecario")

    def format_prompt(past_messages: str, messages: str) -> str:
        message_prompt = f"""
        past interations:
        {past_messages}

        user question: 
        {messages}
        """
        return message_prompt

    if "messages" not in st.session_state:
        st.session_state.messages = [
            {
                "role": "Librarian",
                "content": "Olá! Você precisa de alguma recomendação de livros? Veio ao lugar certo! 👋"
            }
        ]

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):

            regex = r"<showLogs>(\d+)</showLogs>"
            match = re.search(regex, message["content"])
            if match:
                book_id = match.group(1)
                message["content"] = message["content"].replace(match.group(0), "")
                st.markdown(message["content"])
                print_book_logs(book_id)
                continue

            st.markdown(message["content"])


    prompt = st.chat_input("O que você procura?")

    if prompt:
        
        with st.chat_message("You"):
            st.write(prompt)

        st.session_state.messages.append({"role": "user", "content": prompt})
        
        with st.spinner("Esperando resposta do Bibliotecário..."):

            bot_response = get_librarian_response( st.session_state.messages, prompt)

            st.session_state.messages.append({"role": "Librarian", "content": bot_response})
            st.rerun()

if __name__ == "__main__":
    main()