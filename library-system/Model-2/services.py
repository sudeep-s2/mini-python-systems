# Services.py

from Models import Book, User
from Database import load_books, save_books, load_users, save_users

# Load the database into RAM when the server/system starts
books_db = load_books()
users_db = load_users()

def add_new_book(book_id, title, author, total_copies):
    """Processes adding a book and saving to the database."""
    if book_id in books_db:
        return False, "Error: Book ID already exists."
    
    new_book = Book(book_id, title, author, total_copies)
    books_db[book_id] = new_book
    save_books(books_db)
    
    return True, f"Success: '{title}' added to the library."

def add_new_user(user_id, user_name):
    """Processes adding a user and saving to the database."""
    if user_id in users_db:
        return False, "Error: User ID already exists."
    
    new_user = User(user_id, user_name)
    users_db[user_id] = new_user
    save_users(users_db)
    
    return True, f"Success: User '{user_name}' created."