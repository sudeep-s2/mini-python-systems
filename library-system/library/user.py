from library.data import user
def get_user_name():
    while True:
        name = input("Enter the name of the user:")
        if name.strip():
            break
        else:
            print("Invalid input")
            continue
    return name.title()

def get_user_id():
    while True:
        try:
            u_id = int(input("Enter the user id:"))
            if u_id in user:
                print("Duplicate id, please re-enter")
                continue
            else:
                if u_id > 0 :
                    break
                else:
                    print("Not a valid id , please enter a valid id")
                    continue
        except ValueError:
            print("Invalid input, please re-enter")
    return u_id
def validate_user():
    while True:
        try:
            u_id = int(input("Enter the user id:"))
            if u_id in user:
                break
            else:
                print("No user found with the entered id")
        except ValueError:
            print("Invalid user input")
            continue
    return u_id
def get_borrower_details():
    b_name = get_user_name()
    borrower_id = get_user_id()
    pass
def get_returners_details():
    r_name = get_user_name()
    r_id = get_user_id()
    pass
    
    