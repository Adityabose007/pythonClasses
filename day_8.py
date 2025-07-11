'''def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
    
print(fact(5))  # Output: 120'''



#fibonacci series

n = int(input("Enter the number of terms in the Fibonacci series: "))
a, b = 0, 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

# task: 1 - sum of digits with recursion
# task: 2 - sum of natural numbers with recursion






        

