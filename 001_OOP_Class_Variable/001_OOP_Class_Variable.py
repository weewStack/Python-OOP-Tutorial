# Introduction to Python OOP programing: Class Variable / attribute


# 1- Declare the class
class Book:
    # Adding the Class variables
    PaperBased = True
    language = "JP"
    pass


# 2 - Initiate or declarehe instances of the created class
book_1 = Book()
book_2 = Book()

# 3 - Add attribute to the object
book_1.title = "Introduction to the WeeW"
book_1.authors = ["WeeW", "A bunch of other people"]
book_2.title = "7 Habits"
book_2.authors = ["Stephen Covey"]

# print(book_1.language)
# print(book_2.language)

book_1.language = "en"

print(book_1.PaperBased)
print(book_2.PaperBased)


book_2.PaperBased = False
print(book_1.PaperBased)
print(book_2.PaperBased)
