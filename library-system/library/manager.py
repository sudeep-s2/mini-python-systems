book = {}
def addbook():
    while True:
        try:
            b_id = int(input("Enter the book id:"))
            if b_id in book:
                print(f"book id :{b_id} is a duplicate id")
                continue
            else:
                if b_id > 0 :
                    break
                else:
                    print("Not a valid id , please enter a valid id")
                    continue
        except ValueError:
            print("Invalid id")
    name = input("Enter the name of the book:")
    while True:
     if not name.strip():
         break
     else:
         print("Invalid input")
         continue

    a_name = input("Enter the name of the author:")
    while True:
        if not a_name.strip():
            break
        else:
            print("Invalid input")
            continue
    while True:
        try:
            quantity = int(input("Enter the quantity of the book:"))
            if quantity > 0:
                break
            else:
                print("Invalid quantity")
                continue
        except ValueError:
            print("Please enter a valid quantity")
    book[b_id] = {"name": name, "author name": a_name, "quantity": quantity}
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
    pass
def borrowbook():
    pass
def returnbook():
    pass

