# Database.py

import json
import os
from Models import Book, User

BOOKS_FILE = "books.json"
USERS_FILE = "users.json"

def load_books():
    books_dict = {}
    if not os.path.exists(BOOKS_FILE):
        return books_dict 

    with open(BOOKS_FILE, "r") as file:
        raw_data = json.load(file)
        
    for b_id, book_data in raw_data.items():
        rebuilt_book = Book(
            book_id=book_data["book_id"],
            title=book_data["title"], 
            author=book_data["author"],
            total_copies=book_data["total_copies"]
        )
        rebuilt_book.availability = book_data["available_copies"]
        books_dict[int(b_id)] = rebuilt_book
        
    return books_dict

def save_books(books_dict):
    data_to_save = {}
    for b_id, book_obj in books_dict.items():
        data_to_save[b_id] = book_obj.to_dict()
        
    with open(BOOKS_FILE, "w") as file:
        json.dump(data_to_save, file, indent=4)

# (Assume load_users and save_users follow this exact same pattern)