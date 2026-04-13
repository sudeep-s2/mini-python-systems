from library.data import book, user
from library.book import get_id, get_aname, get_name, get_quantity
from library.user import get_user_name, get_user_id
def addbook():
    b_id = get_id()
    name = get_name()
    a_name = get_aname()
    quantity = get_quantity()
    available = quantity
    book[b_id] = {"name": name.title(), "author name": a_name.title(), 
                  "quantity": quantity, "availability": available, "Borrowed by": None}
    print("Book added successfully")
def displayall():
    for items, info in book.items():
        print(f"BOOK Details: {items} {info}")
def search():
    target = int(input("Enter the book id:"))
    if target in book:
        print(f"{book[target]}")
    else:
        print("The mentioned id is not a valid id , please enter a valid id")
def deletebook():
    target = get_id()
    if target in book:
        del book[target]
        print(f"Deleted the book, with the mentioned id{target}")
    else:
        print("Enter a valid book id")
def add_user():
    name = get_user_name()
    u_id = get_user_id()
    user[u_id] = {"User_name": name, "Books_borrowed": {}}
    print(f"{name} is now a user at this library and your user id is{u_id}")
def delete_user():
    while True:
        name = get_user_name()
        u_id = get_user_id()
        if u_id in user:
            del user[u_id]
            print(f"{name} with id {u_id} is now not a user at this library")
            break
        else:
            print("Invalid user id, please enter a valid id")
            continue

def modify_user():
    u_id = get_user_id()
    if u_id in user:

        if (mod := input("Modify (name/user_id): ").lower()) == "name":
            user[u_id]["name"] = get_user_name()

        elif mod == "user_id":
            # user[u_id] = input("Enter new user_id: ")
            pass

        else:
            print("Invalid modification option")
        print(f"The record {u_id} for user {user[u_id]['name']} is modified")

    else:
        print("User not found")


def borrowbook():
    u_id = get_user_id()
    if u_id in user:
        book_id = get_id()
        if book_id in book:
            if book[book_id]["availability"] > 0:
                book[book_id]["availability"]-=1
                if user[u_id]["Books_borrowed"] is None:
                    user[u_id]["Books_borrowed"] = {book_id: 1}
                else:
                    if book_id in user[u_id]["Books_borrowed"]:
                        user[u_id]["Books_borrowed"][book_id] += 1
                    else:
                        user[u_id]["Books_borrowed"][book_id]= 1
            else:
                print("For the selected book, no more copies are left")
        else:
            print("Book id is invalid or wrong")
    else:
        print('Invalid user')

def returnbook():
    u_id = get_user_id()

    if u_id in user:

        book_id = get_id()

        if user[u_id]["Books_borrowed"] and book_id in user[u_id]["Books_borrowed"]:

            user[u_id]["Books_borrowed"][book_id] -= 1
            book[book_id]["availability"] += 1

            if user[u_id]["Books_borrowed"][book_id] == 0:
                del user[u_id]["Books_borrowed"][book_id]

            print("Book returned successfully")

        else:
            print("This user didn't borrow this book")

    else:
        print("Invalid user")

