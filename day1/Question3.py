# Q3: Factorial of a number

n = int(input("Enter a number: "))

factorial = 1   # start from 1

for i in range(1, n + 1):    # loop from 1 to n
    factorial = factorial * i  # multiply each number

print("Factorial =", factorial)