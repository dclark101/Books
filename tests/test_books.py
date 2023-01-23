import pytest
import os
from scripts.books import Books
from dotenv import load_dotenv
load_dotenv()

# API_KEY for testing
API_KEY = os.environ.get("API_KEY")
# Faulty URL for testing
url: str = f"htps://www.googleapis.com/books/v1/volumes?q=search+intitle:Harry&key={API_KEY}"


def test_if_api_key_exists():
    assert os.environ.get("API_KEY") != None


def test_if_fetch_reraises_exception():
    books_data = Books(os.environ.get("API_KEY"))
    with pytest.raises(Exception):
        books_data.fetch(url)
