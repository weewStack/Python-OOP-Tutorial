# Introduction to Python OOP programing: Dunder - Magic  Special Method __init__

# A dunder or magic Method shape: __SpecialMehtodName__

# 1- Declare the class


class Book:
    # Adding the Class variables
    PaperBased = True
    language = "JP"

    def __init__(self, title, authors, rating):
        self.title = title
        self.authors = authors
        self.rating = rating

    # Adding a normal method: A methond is a function attached to the instances
    # It have a special format by introducing the new variable self

    # Return some stuff, same as a normal function
    def authorsSTR(self):
        return ", ".join(self.authors)
    # Initiate an object attribute

    def addFavorite(self):
        self.isFavorite = True
    # Transform an attribute

    def ImproveRate(self):
        self.rating = min(10, self.rating+1)

    def DowngradeRate(self):
        self.rating = max(0, self.rating-1)


# 2 - Initiate or declarehe instances of the created class
book_1 = Book("Introduction to the WeeW", [
              "WeeW", "A bunch of other people"], 4)
book_2 = Book("7 Habits", ["Stephen Covey"], 4)

# 3 - Add attribute to the object
print(book_1.authors)
print(book_2.title)
print(book_1.rating)
print(book_2.rating)
book_1.ImproveRate()
book_2.DowngradeRate()
print(book_1.rating)
print(book_2.rating)
