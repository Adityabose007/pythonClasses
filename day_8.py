'''def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
    
print(fact(5))  # Output: 120'''



#fibonacci series

'''n = int(input("Enter the number of terms in the Fibonacci series: "))
a, b = 0, 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b'''

# task: 1 - sum of digits with recursion

def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + sum_of_digits(n // 10)
print(sum_of_digits(512))

# task: 2 - sum of natural numbers with recursion

def sum_natural(n):
    if n == 0:
        return 0
    else:
        return n + sum_natural(n - 1)

print(sum_natural(10))






        

