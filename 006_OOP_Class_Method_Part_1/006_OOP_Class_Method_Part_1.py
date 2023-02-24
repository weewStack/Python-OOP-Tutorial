# Introduction to Python OOP programing: Class method Part-1

# @classmethod & need the "cls" argument
# @ is a function decorator


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


# 2 - Initiate or declarehe instances of the created class
book_1 = Book("Introduction to the WeeW", [
              "WeeW", "A bunch of other people"], "A great book", 454)
book_2 = Book("7 Habits", ["Stephen Covey"], "Best book of the year", 234)

Book.change_lang("EN")
print(book_1.language)
print(book_2.language)

BookInfo = {"title": "The WeeW life", "authors": [
    "WeeW"], "description": "A nice book", "pageCount": 334}

book_3 = Book.CreateBook(BookInfo)
print(book_3.__dict__)
