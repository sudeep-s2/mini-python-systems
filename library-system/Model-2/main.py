# Main.py

import services

def admin_menu():
    while True:
        print("\n--- Admin Menu ---")
        print("1. Add Book")
        print("2. Add User")
        print("3. Return to Main Menu")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            try:
                b_id = int(input("Enter Book ID: "))
                title = input("Enter Title: ")
                author = input("Enter Author: ")
                copies = int(input("Enter Total Copies: "))
                
                # Pass data to services.py (The Brain)
                is_success, message = services.add_new_book(b_id, title, author, copies)
                
                # Print what the Brain returns
                print(message)
                
            except ValueError:
                print("Invalid input! Please enter numbers for ID and Copies.")
                
        elif choice == "2":
            # (User input logic here calling services.add_new_user)
            pass
            
        elif choice == "3":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    # Start the system
    admin_menu()