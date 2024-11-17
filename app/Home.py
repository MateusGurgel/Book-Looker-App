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

def main():
    st.title("Book Looker")
    st.markdown("## Home em construção")


if __name__ == "__main__":
    main()