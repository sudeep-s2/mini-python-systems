#Helping methods
from library.data import book
def get_name():
    while True:
        name = input("Enter the name of the book:")
        if name.strip():
            break
        else:
            print("Invalid input")
            continue
    return name.title()

def get_id():
    while True:
        try:
            b_id = int(input("Enter the book id:"))
            if b_id in book:
                print("Duplicate id, please re-enter")
                continue
            else:
                if b_id > 0 :
                    break
                else:
                    print("Not a valid id , please enter a valid id")
                    continue
        except ValueError:
            print("Invalid input, please re-enter")
    return b_id
def get_aname():
    a_name = input("Enter the name of the author of the book:")
    while True:
        if a_name.strip():
            break
        else:
            print("Invalid input, please re-enter")
            continue
    return a_name.title()
def get_quantity():
    while True:
        try:
            quantity = int(input("Enter the quantity of the book:"))
            if quantity > 0:
                break
            else:
                print("please re-enter")
                continue
        except ValueError:
            print("Invalid input, please re-enter")
            continue
    return quantity
        