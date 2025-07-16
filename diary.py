# diary.txt
# date, line

# inputentry

'''def write_entry():
    date = input("Enter the date (DD-MM-YYYY): ")
    line = input("Write your diary entry: ")

    entry = f"{date} --> {line}\n"

    try:
        with open("diary.txt", "a") as file:
            file.write(entry)
        print("✅ Entry saved successfully!😊")
    except Exception as e:
        print("❌ Failed to write entry:", e)

# Start collecting entries directly
while True:
    write_entry()
    choice = input("Do you want to add another entry? (y/n): ").strip().lower()
    if choice != "y":
        print("👋 Exiting Diary. Goodbye!")
        break'''


def add_entry():
    date = input("Enter the date (DD-MM-YYYY): ")
    line = input("Write your diary entry: ")
    with open("diary.txt", "a") as file:
        file.write(f"#{date} --> {line}")

def view_entry():
    try:
        with open("diary.txt", "r") as file:
            entries = file.readlines()
        if not entries:
            print("No entries found.")
        else:
            print("\n your journal entries:")
        for entry in entries:
            print(entry.strip())
    except:
        print("diary.txt not found!!!")

def main():
    while True:
        print("\nDiary Menu:")
        print("\n1. Add Entry")
        print("\n2. View Entries")
        print("\n3. Exit")
        choice = int(input("Enter your choice (1/2/3): "))
        if choice == 1:
           add_entry()
        elif choice == 2:
            view_entry()
        elif choice == 3:
            print("👋 Exiting Diary. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")
main()