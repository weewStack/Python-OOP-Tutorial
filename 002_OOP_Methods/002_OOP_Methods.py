# Introduction to Python OOP programing: The "Normal" Methods

# object.method_name(arguments)

# 1- Declare the class


class Book:
    # Adding the Class variables
    PaperBased = True
    language = "JP"

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
book_1 = Book()
book_2 = Book()

# 3 - Add attribute to the object
book_1.title = "Introduction to the WeeW"
book_1.authors = ["WeeW", "A bunch of other people"]
book_2.title = "7 Habits"
book_2.authors = ["Stephen Covey"]
book_1.rating = 5
book_2.rating = 5

print(book_1.rating)
print(book_2.rating)
book_1.ImproveRate()
book_2.DowngradeRate()
print(book_1.rating)
print(book_2.rating)
