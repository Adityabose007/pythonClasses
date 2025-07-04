
n=int(input("enter a number"))
number =[]

for i in range(n):
    num=int(input("Enter any number for the list"))
    number.append(num)
    print(number)

avg=sum(number)/len(number)
print(avg)