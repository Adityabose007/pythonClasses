# diary.txt
# date, line

# inputentry




def write_entry():
    date = input("Enter the date (YYYY-MM-DD): ")
    line = input("Write your diary entry: ")

    entry = f"{date} --> {line}\n"

    try:
        with open("diary.txt", "a") as file:
            file.write(entry)
        print("✅ Entry saved successfully!")
    except Exception as e:
        print("❌ Failed to write entry:", e)

# Start collecting entries directly
while True:
    write_entry()
    choice = input("Do you want to add another entry? (y/n): ").strip().lower()
    if choice != "y":
        print("👋 Exiting Diary. Goodbye!")
        break
