# Task : 1 (odd even separator) 
'''n = int(input("Enter the number of elements: "))
numbers = []
odd = []
even = []

for  i in range(n):
    num = int(input("Enter a number: "))
    numbers.append(num)
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
print("Odd numbers:", odd)  
print("Even numbers:", even)'''


#Task : 2 (ph no with name and contact number printing)

'''ph_book = {}
n = int(input("Enter the number of contacts: "))
for i  in range(n):
    name = input("Enter the name: ")    
    ph_no = input("Enter the phone number: ")
    ph_book[name] = ph_no

print(ph_book)'''


#strings 

#[string : ending : step]
'''str = "python is fun"
print(str[2])
print(str[-2])
print(str[2:5])
print(str[:4])
print(str[4:])
print(str[::-1])
print(str[::2])'''


#lower()
str = "python "
'''print(str.lower())
print(str.upper())
print(str.replace("PYTHON", "coding"))
print(str.replace("U", "A"))

str_2 = "Hello World"
print(str_2.replace('o', 'a'))'''

#split()
str2 = "Hello World"
'''print(str.split())

print(str.split('o'))'''


#concatenation

'''newStr = str2 + str
print(newStr)

print(len(str2))

for i in str:
    print(i, end=' ')'''

'''if ("tho" in str):
    print("is present")
else:
    print("is not present")


num = "124"
num2 = "12a4"

print(num.isdigit())
print(num2.isdigit())'''

'''alpha = "HEllo"
alpha_2 = "HEllo123"
print(alpha.isalpha())
print(alpha_2.isalpha())

alphanum = "Alpha123"
print(alphanum.isalnum())'''


'''print(str2.find("o"))

print(sorted(str2))


var  = sorted(str2)

print(var[3])'''



# find vowels in a string

'''str = input("Enter a string: ")
result = ""
vowels = "aeiouAEIOU"
vowelCount = 0
conCount = 0
for char in str:
    if (char in vowels):
        vowelCount += 1
    else:
        conCount += 1
        #print(char, end=' ')
        result = result + char
        print(result)

    
print("Number of vowels:", vowelCount)
print("Number of consonants:", conCount)
print("Consonants in the string:", result)'''


#digit extraction

str2 = input("Enter a string with digits: ")
digits = ""
for char in str2:
    if char.isdigit():
        digits += char
print("Extracted digits:", digits)

str = input("Enter the string: ")
digiCount = 0
digit = ''
#digit = "123456"
#result = ""
for i  in str:
    if i.isdigit():
        difiCount += 1
        digit = digit +i

print(digiCount)
print(digit)
#print(result)

#task 1: palindrome check
#racecar
#racecar


#task 2: anagram check
#listen
#silent

#task 3: python is on trend
#remove duplicates characters