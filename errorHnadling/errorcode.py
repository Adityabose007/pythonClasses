# error handling
# try, except


#print(10/0)

try:
    a= 100
    a = a/0
    print(a)
except Exception as e:
    print("Error: you can't divide a number by zero.\n")
    print("try again")
    print("some error occurred =", e)
    
    # You can also log the error or handle it in a specific way
    # For example, you could log the error to a file or raise a custom exception


'''if (a<18):
    print("You are eligible to vote")
    a = a/10
else:
    print("You are not eligible to vote")
    a = a/0'''


'''try:
    file = open("fileisnot.txt", "r")
    content = file.read()
    print(content)
except :
    print("Error: The file does not exist or cannot be opened.")'''




