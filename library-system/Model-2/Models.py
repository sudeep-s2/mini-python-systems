# Models.py/Data Structure Part

class Book:
    def __init__(self, book_id, name, author, quantity):
        self.book_id = book_id
        self.name = name
        self.author = author
        self.quantity = quantity
        self.availability = quantity
    def to_dict(self):
        return {"book_id" : self.book_id,
                "title" : self.name,
                "author" : self.author,
                "total_copies": self.quantity,
                "available_copies": self.availability}
class User:
    def __init__(self, user_id, user_name):
        self.user_id = user_id
        self.user_name = user_name
        self.books_borrowed = {}
    def to_user_dict(self):

        return {"User_id" : self.user_id,
                "User_name": self.user_name,
                "Books_borrowed": self.books_borrowed}