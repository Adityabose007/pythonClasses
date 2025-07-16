import booksManage
import personManage

def main_menu():
    while True:
        print("\n====== Library Management System ======")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Add Person")
        print("4. Remove Person")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            number = input("Enter Book Number: ")
            name = input("Enter Book Name: ")
            booksManage.add_book(number, name)
        
        elif choice == "2":
            number = input("Enter Book Number to remove: ")
            booksManage.remove_book(number)

        elif choice == "3":
            lib_id = input("Enter Library ID: ")
            name = input("Enter Person Name: ")
            personManage.add_person(lib_id, name)

        elif choice == "4":
            lib_id = input("Enter Library ID to remove: ")
            personManage.remove_person(lib_id)

        elif choice == "5":
            print("👋 Exiting Library System. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main_menu()
