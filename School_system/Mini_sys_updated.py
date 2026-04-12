data = {}
def get_roll():
    while True:
        try:
            roll = int(input("Enter the roll number of the student:"))
            return roll
        except ValueError:
            print("Invalid input, please enter the roll number of the studnet interms of number")

def get_name():
    while True:
        name = input("Enter the name of the student:").strip().lower()
        if name.replace(" ","").isalpha():
            return name.title()
        else:
            print('Invalid input, please enter alphabets only , no special character or numbers are allowed')
def get_grade():
    valid =['A','A++','A+','B','C','D']
    while True:
        grade = input("Enter the grade of the student in lower or upper case:").upper()
        if grade in valid:
            return grade
        else:
            print("Invalid grade")
n = int(input("Enter the number of students in the class:"))
for i in range(n):
    roll = get_roll()
    name = get_name()
    grade = get_grade()
    data[roll]= {"name": name, "grade": grade}
for roll, info in data.items():
    print(roll, info)
def add():
    roll = get_roll()
    name = input("Enter the name of student")
    if name.replace(" ","").isalpha():
        pass
    else:
        print("Invalid input, please enter a valid input alphabets only")
    valid =['A','A++','A+','B','C','D']
    while True:
        grade = input("Enter the grade of the student in lower or upper case").upper()
        if grade in valid:
            break
        else:
            print("Invalid grade")
    data[roll] = {"name": name, "grade": grade}
    print(f" Updated data is {data}")
def delete():
    roll = get_roll()
    if roll in data:
        del data[roll]
    else:
        print("Invalid roll number")
def modify():
    roll = get_roll()
    if roll in data:

        if (mod := input("Modify (name/grade): ").lower()) == "name":
            data[roll]["name"] = input("Enter new name: ")

        elif mod == "grade":
            data[roll]["grade"] = input("Enter new grade: ")

        else:
            print("Invalid modification option")
        print(f"The record {roll} for student {data[roll]['name']} is modified")

    else:
        print("Student not found")
def display():
    n = int(input("Enter the number records you wanted:"))

    for i in range(n):
        key = get_roll()

        # FIXED: avoid KeyError
        if key in data:
            print(f"The record {key} and data is {data[key]}")
        else:
            print("Student not found")

    print("The given number of data is shown successfully")
def displayall():
    for roll, info in data.items():
        print(roll, info)
    print("All records from data is displayed")
def sortdata():
    print("1. Sort by Name")
    print("2. Sort by Roll_No")
    print("3. Sort by Grade")

    choice = input("Enter the choice:")

    match choice:

        case "1":
            for roll, info in sorted(data.items(), key=lambda x: x[1]["name"]):
                print(roll, info)

        case "2":
            for roll in sorted(data):
                print(roll, data[roll])

        case "3":
            for roll, info in sorted(data.items(), key=lambda x: x[1]["grade"]):
                print(roll, info)

        case _:
            print("Invalid choice, choose another")

    print("Sorting is done based on your choice")
def search():
    search = get_roll()

    if search in data:
        print(data[search])
    else:
        print("Student not found")
def menu():
    print("Menu".center(24))
    print("1. Add Record")
    print("2. Delete Record")
    print("3. Modify Record")
    print('4. Display record(One or more)')
    print("5. To display all records")
    print("6. Sort")
    print("7. Search")
    print("8. Exit")

while True:
    menu()
    choice = input("Enter the choice:")
    match choice:
        case "1":
            add()
        case "2":
            delete()
        case "3":
            modify()
        case "4":
            display()
        case "5":
            displayall()
        case "6":
            sortdata()
        case "7":
            search()
        case "8":
            break
        case _:
            print("Invalid choice, please select a valid options from menu")

