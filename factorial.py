def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n-1)

n=3
print(factorial(n))