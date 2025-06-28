a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = input("Enter operator (+, -, *, /): ")

if c == "+":
    print(a + b)
elif c == "-":
    print(a - b)
elif c == "*":
    print(a * b)
elif c == "/":
    if b != 0:
        print(a / b)
    else:
        print("Division by zero is not allowed")
else:
    print("Invalid operator!")

