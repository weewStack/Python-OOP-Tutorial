# Introduction to Python OOP programing: Class method Part-2: API example

# Using Python native library "urllib.request" & "json"

import urllib.request
import json


class Book:
    # Adding the Class variables
    PaperBased = True
    language = "JP"

    def __init__(self, title, authors, description, pageCount):
        self.title = title
        self.authors = authors
        self.description = description
        self.pageCount = pageCount

    def __str__(self):
        # __str__ method
        return self.title + " by " + self.authorsSTR()

    def authorsSTR(self):
        # Return some stuff, same as a normal function
        return ", ".join(self.authors)

    def addFavorite(self):
        # Initiate an object attribute
        self.isFavorite = True

    def ImproveRate(self):
        # Transform an attribute
        self.rating = min(10, self.rating+1)

    def DowngradeRate(self):
        self.rating = max(0, self.rating-1)

    @staticmethod
    def is_expensive(price):
        if price > 10:
            return True
        else:
            False

    @classmethod
    def change_lang(cls, lang):
        cls.language = lang

    @classmethod
    def CreateBook(cls, data):
        title = data["title"]
        authors = data["authors"]
        description = data["description"]
        pageCount = data["pageCount"]
        return cls(title, authors, description, pageCount)


# 1 - Get the API data
# Link: https://www.googleapis.com/books/v1/volumes?q=intitle:7%20Habit&langRestrict=en&maxResults=40

bookName = input("Provide a book title: ")
url_title = bookName.replace(" ", "%20")
url = f"https://www.googleapis.com/books/v1/volumes?q=intitle:{url_title}&langRestrict=en&maxResults=40"
response = urllib.request.urlopen(url)
data = json.loads(response.read().decode())

# print(data)

for item in data["items"]:
    try:
        mybook = Book.CreateBook(item["volumeInfo"])
        print(mybook)
    except Exception as e:
        print(e)
