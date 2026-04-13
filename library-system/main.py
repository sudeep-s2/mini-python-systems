from library.manager import (
    addbook,
    deletebook,
    displayall,
    search,
    add_user,
    delete_user,
    modify_user,
    borrowbook,
    returnbook
)
def admin_menu():
    while True:
        print("\n ---   Admin Menu   ---")
        print("1. Add book")
        print("2. Delete book")
        print("3. Add User")
        print("4. Delete user")
        print("5. Display all books")
        print("6. Exit")
        choice = input("Enter choice: ")

        match choice:
            case "1":
                addbook()
            case "2":
                deletebook()
            case "3":
                add_user()
            case "4":
                delete_user()
            case "5":
                displayall()
            case "6":
                break
            case _:
                print("Invalid choice")


def user_menu():
    while True:
        print("\n--- User Menu ---")
        print("1. Borrow book")
        print("2. Return book")
        print("3. Search book")
        print("4. Modify user data")
        print("5. View available books")
        print("6. Exit")
        choice = input("Enter choice: ")

        match choice:
            case "1":
                borrowbook()
            case "2":
                returnbook()
            case "3":
                search()
            case "4":
                modify_user()
            case "5":
                displayall()
            case "6":
                break
            case _:
                print("Invalid choice")


def main():
    while True:
        print("\n--- Library System ---")
        print("1. Admin")
        print("2. User")
        print("3. Exit")

        choice = input("Enter choice: ")

        match choice:
            case "1":
                admin_menu()
            case "2":
                user_menu()
            case "3":
                print("Exiting...")
                break
            case _:
                print("Invalid choice")


if __name__ == "__main__":
    main()