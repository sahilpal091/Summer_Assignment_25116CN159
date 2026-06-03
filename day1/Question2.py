# Q2: Multiplication table of a given number

n = int(input("Enter a number: "))

for i in range(1, 11):   # loop from 1 to 10
    print(n, "x", i, "=", n * i)