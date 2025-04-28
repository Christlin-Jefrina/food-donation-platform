def factorial(n):
    if n < 0:
        return None
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

# Test cases
print(factorial(5) == 120)
print(factorial(0) == 1)
print(factorial(-3) == None)
