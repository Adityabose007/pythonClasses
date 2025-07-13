# task: 1 - list 5 nmae user input string (write + read) 

# Write 5 names to file
with open("names.txt", "w") as f:
    for i in range(5):
        name = input(f"Enter name {i+1}: ")
        f.write(name + "\n")

# Read and print names from file
with open("names.txt", "r") as f:
    print("Names in file:")
    for line in f:
        print(line.strip())

# task: 2 - multiplication table (write + read)

num = int(input("Enter a number for multiplication table: "))

# Write multiplication table to file
with open("table.txt", "w") as f:
    for i in range(1, 11):
        line = f"{num} x {i} = {num * i}\n"
        f.write(line)

# Read and print multiplication table from file
with open("table.txt", "r") as f:
    print(f"Multiplication table of {num}:")
    for line in f:
        print(line.strip())