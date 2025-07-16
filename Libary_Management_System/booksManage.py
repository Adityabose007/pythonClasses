def add_book(number, name):
    with open("Books.txt", "a") as file:
        file.write(f"{number},{name}\n")
    print("✅ Book added.")

def remove_book(number):
    lines = []
    with open("Books.txt", "r") as file:
        lines = file.readlines()

    with open("Books.txt", "w") as file:
        found = False
        for line in lines:
            if not line.startswith(f"{number},"):
                file.write(line)
            else:
                found = True
        if found:
            print("✅ Book removed.")
        else:
            print("⚠️ Book not found.")