'''# function declaration
def greet():
    print("Hello, World!")

#calling 
greet()    '''

#declaration
'''def name(name, a): #arguments
    print("Name is ", name)
    print("Age is ", a)
    mul = a * 10
    return mul

#calling
value = name("john", 25) #parameter
print("the value returned from function is", value)'''

#print(name("john", 25)) #parameter


#project

'''start = int(input("Enter the Starting point: "))
end = int(input("Enter the Ending point: "))

#5 - 10
#5 7

def prime(start, end):
    print(f"The prime numbers between {start} and {end} are:")
    for i in range(start, end + 1):
        if is_prime(i):
            print(i)



def is_prime(data):
    if data <=1:
        return False
    else:
        #d = int()
        for i in range(2,data):
            if data%i == 0:
                return False
    return True

prime(start ,end)'''

#task : calculator 
# handled by zero
# use menu () for user input
# user = 1 2 3
#1. add
#2. mul
#3. div

#if 1
#add ()
#if 2
#mul ()
#if 3
#div ()

#enter 1
#enter 2

#add()
#enter 1
#enter 2

#print()


# ...existing code...

'''print("------Welcome to the Calculator----")
def add(a, b):
    return a + b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def menu():
    print("Calculator Menu:")
    print("1. Add")
    print("2. Multiply")
    print("3. Divide")
    choice = input("Enter your choice (1/2/3): ")
    return choice

def calculator():
    choice = menu()
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if choice == "1":
        print("Result:", add(num1, num2))
    elif choice == "2":
        print("Result:", mul(num1, num2))
    elif choice == "3":
        print("Result:", div(num1, num2))
    else:
        print("Invalid choice. Please select 1, 2, or 3.")

calculator()'''



''' x = lambda a: a * 10
print(x(5))

y = lambda num1, num2: num1 + num2
print(y(5, 10)) 

z = lambda d, e, f:(d * e) + f
value = z(2, 10, 5)
print(value)'''

'''def countDown(n):
    if n <= 0:
        print("Countdown finished!")
    else:
        print(n)
        countDown(n - 1)  # recursive call
countDown(5)  # Start the countdown from 5'''


#task 1 - leap year

# Check if a year is a leap year

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

year = int(input("Enter a year: "))
if is_leap_year(year):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")

#task 2 - simple interest caluclator

#task 2 - simple interest calculator
# Simple Interest Calculator

p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time (in years): "))

si = (p * r * t) / 100
print("Simple Interest is:", si)

#task 3 - number guessing game

# Number Guessing Game

import random

number = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10: "))

if guess == number:
    print("Congratulations! You guessed it right.")
else:
    print(f"Sorry, the correct number was {number}. Better luck next time!")

#task 4 - sum of digits

# Sum of digits

n = int(input("Enter a number: "))
total = 0

while n > 0:
    digit = n % 10
    total += digit
    n = n // 10

print("Sum of digits is:", total)

'''n = 1 2 5 6
n % 10 = 6
n / 10 = 125

a = n/10 =125

a % 10 = 5
a / 10 = 12'''