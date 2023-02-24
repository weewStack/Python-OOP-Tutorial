# Introduction to Python OOP programing: Class Inheritance

# Getting some free code from a parent class

# When there is a need of topic diversity and limit code bulkiness


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

# Declare a sub classes


class Essay(Book):
    def __init__(self, title, authors, description, pageCount, genre, style):
        super().__init__(title, authors, description, pageCount)
        self.genre = genre
        self.style = style

    def __str__(self):
        # __str__ method
        return "Essay: " + self.title + " by " + self.authorsSTR()
# Declare another sub classes


class Thesis(Book):
    def __init__(self, title, authors, description, pageCount, field, university):
        super().__init__(title, authors, description, pageCount)
        self.field = field
        self.university = university

    def __str__(self):
        # __str__ method
        return "Thesis: " + self.title + " by " + self.authorsSTR() + " at " + self.university


ess_1 = Essay("A tale of WeeW", ["Someone"],
              " A nice story", 213, "syfi", "Modern")
th_1 = Thesis("How to count", [
              "WeeW"], "May be we count in the wrong", 50, "History", "MIT")

print(ess_1)
print(th_1)

# print(help(ess_1))
