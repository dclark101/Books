import books

import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.environ.get("API_KEY")

google_books = books.Books(API_KEY)

google_books.search("inauthor", "J.K. Rowling")
