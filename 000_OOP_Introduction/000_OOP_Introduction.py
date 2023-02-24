# Introduction to Python OOP programing: Class - Instance - attributes


# 1- Declare the class
class Book:
    pass


# 2 - Initiate or declarehe instances of the created class
book_1 = Book()
book_2 = Book()

# print(book_1)
# print(book_2)

# 3 - Add attribute to the object
book_1.title = "Introduction to the WeeW"
book_1.authors = ["WeeW", "A bunch of other people"]

print(book_1.title)
print(book_1.authors)
book_2.title = "7 Habits"
book_2.authors = ["Stephen Covey"]
print(book_2.title)
print(book_2.authors)
