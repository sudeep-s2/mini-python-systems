data = {}

n = int(input("Enter the number of the students in the class:"))
for i in range(n):
    name = input("Enter the name:")
    roll_no = int(input("Enter the roll no of the given student:"))
    grade = input('Enter the grade of the student:')
    data[roll_no] = {"name": name, 'grade': grade}


def add():
    roll = int(input("Enter the roll no:"))

    if roll in data:
        print("already exist")
    else:
        name = input("Enter the name:")
        grade = input("Enter the grade of the student:")

        # FIXED: indentation mistake — previously outside else block
        # FIXED: removed "grade " extra space key mistake
        data[roll] = {"name": name, "grade": grade}

        print(f"The new record with the roll no: {roll} is added to the data")


def delete():
    roll = int(input("Enter the roll no of the student whose record is wanted to be removed:"))

    if roll not in data:
        print("No student found")
    else:
        del data[roll]

        # FIXED: previously printing delete message even when not deleted
        print(f"The {roll} is deleted from data")


def modify():
    roll = int(input("Enter the roll no:"))

    if roll in data:

        # FIXED WALRUS USAGE
        # Previously: mod := input(...) == "name"  (wrong)
        # Now: store input first, then compare

        if (mod := input("Modify (name/grade): ").lower()) == "name":
            data[roll]["name"] = input("Enter new name: ")

        elif mod == "grade":
            data[roll]["grade"] = input("Enter new grade: ")

        else:
            print("Invalid modification option")

        # FIXED: syntax error due to nested quotes
        print(f"The record {roll} for student {data[roll]['name']} is modified")

    else:
        print("Student not found")


def display():
    n = int(input("Enter the number records you wanted:"))

    for i in range(n):
        key = int(input("Enter the roll number of the student:"))

        # FIXED: avoid KeyError
        if key in data:
            print(f"The record {key} and data is {data[key]}")
        else:
            print("Student not found")

    print("The given number of data is shown successfully")


def displayall():
    # IMPROVED: better formatting instead of printing dictionary directly
    for roll, info in data.items():
        print(roll, info)
    print("All records from data is displayed")


def sorting_a():
    print("1. Sort by Name")
    print("2. Sort by Roll_No")
    print("3. Sort by Grade")

    choice = input("Enter the choice:")

    match choice:

        # FIXED: previously sorting by roll instead of name
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
    search = int(input("Enter the roll number of the student what you was searching:"))

    # FIXED: avoid KeyError
    if search in data:
        print(data[search])
    else:
        print("Student not found")


def menu():
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
            sorting_a()

        case "7":
            search()

        case "8":
            break

        case _:
            print("Invalid Choice, Try different choice option from the above menu")