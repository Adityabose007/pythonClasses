#for(int i =0; i<=10; i++)
#for i in range(start, stop, step):
    
'''for i in range(5):
    print(i)'''

'''num = 5
a = 1

if (num<0):
        print("Factorial is not defined for negative numbers")
elif (num == 0 or num == 1):
        print("Factorial is 1")
for i in range(2, num + 1):
        a *= i
print("Factorial is", a)'''



'''a = 0 
b = 1
n = 10
for i in range(n): 
    print(a, end=' ')
    a,b = b, a+b'''

'''count = 0
a = "AEIOUaeiou"
for i in "Light":
    if i in a:
        count += 1
print(count)'''

'''x = 1
while x <= 10:
    print(x, end=' ')
    x += 1'''

'''password = ""
while password != "12345":
        password = input("Enter the password: ")
        if password == "12345":
                print("Access granted")
        else:
                print("Access denied, try again")'''




#switch case example in python

'''var = 2
match var:
    case 1:
        print("the value is 1")
    case 2:
        print("the value is 2")
    case _:
        print("invalid case")'''

Season = input("Enter the season number (1:summer, 2:winter, 3:spring, 4:autumn,5:monsoon): ")
match Season:
    case 1:
        print("It's summer")
    case  2:
        print("It's winter")
    case 3:
        print("It's spring")
    case 4:
        print("It's autumn")
    case 5:
        print("It's monsoon")
    case _:
        print("Invalid season number")
        


    


           
