from scripts.books import Books
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.environ.get("API_KEY")

google_books = Books(API_KEY)
book_data = google_books.search("intitle", "Harry Potter")

print(google_books.book_info(book_data))
