import requests


class Books:

    def __init__(self, key):
        self.key = key

    def search(self, by, query):
        """Searches Google Books API

        Args:
            by (string): searches by intitle, inauthor, or inpublisher
            query (string): provides descriptive search result for by
        """

        url = self.loc_book = f"https://www.googleapis.com/books/v1/volumes?q=search+{by}:{query}&key={self.key}"

        try:
            res = requests.get(url)
        except requests.exceptions.HTTPError as e:
            print(e)
        else:
            print(res.json())
