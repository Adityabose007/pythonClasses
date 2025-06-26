def calculator(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b
    else:
        return ("Invalid operator")

print(calculator(10, 5, '+'))  # Output: 15
print(calculator(10, 5, '-'))  # Output: 5
print(calculator(10, 5, '*'))  # Output: 50
print(calculator(10, 5, '/'))  # Output: 2.0




# Variable assignment and comment
name = "Aditya"
age = 20
rating = 4.5

# Print the values
print("Name:", name)
print("Age:", age)
print("Rating:", rating)

# Check data types
print(type(name))  # str
print(type(age))   # int
print(type(rating))  # float
