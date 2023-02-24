# Introduction to Python OOP programing: Static method

# @staticmethod & Doesn't need the "self" argument
# @ is a function decorator

# 1- Declare the class


class Book:
    # Adding the Class variables
    PaperBased = True
    language = "JP"

    def __init__(self, title, authors, rating):
        self.title = title
        self.authors = authors
        self.rating = rating

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


# 2 - Initiate or declarehe instances of the created class
book_1 = Book("Introduction to the WeeW", [
              "WeeW", "A bunch of other people"], 4)
book_2 = Book("7 Habits", ["Stephen Covey"], 4)

print(book_1.is_expensive(12))
print(book_2.is_expensive(8))
