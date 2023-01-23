import requests
from typing import Any


class Books:

    def __init__(self, key):
        self.key = key
        self.books = []

    def fetch(self, url: str) -> requests.Response:
        try:
            res: requests.Response = requests.get(url)
        except requests.exceptions.HTTPError as e:
            print(e)
        else:
            return res

    def search(self, by: str, query: str):
        """Searches Google Books API

        Args:
            by (string): searches by intitle, inauthor, or inpublisher
            query (string): provides descriptive search result for by
        """
        url: str = f"https://www.googleapis.com/books/v1/volumes?q=search+{by}:{query}&key={self.key}"
        return self.fetch(url).json()

    def book_info(self, book):

        try:
            items = book["items"]

        except KeyError as e:
            print(f"Key does not exist {e}")
        else:
            for i in range(len(items) - 1):
                title: str = book["items"][i]["volumeInfo"]["title"]
                description: str = book["items"][i]["volumeInfo"]["description"]

                self.books.append({"title": title,
                                  "description": description})
            return self.books
