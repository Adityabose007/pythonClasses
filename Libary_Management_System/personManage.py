def add_person(lib_id, name):
    with open("Person.txt", "a") as file:
        file.write(f"{lib_id},{name}\n")
    print("✅ Person added.")

def remove_person(lib_id):
    lines = []
    with open("Person.txt", "r") as file:
        lines = file.readlines()

    with open("Person.txt", "w") as file:
        found = False
        for line in lines:
            if not line.startswith(f"{lib_id},"):
                file.write(line)
            else:
                found = True
        if found:
            print("✅ Person removed.")
        else:
            print("⚠️ Person not found.")