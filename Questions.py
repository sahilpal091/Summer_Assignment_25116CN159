# Q1: Sum of first N natural numbers

n = int(input("Enter the value of N: "))

sum = 0  # start sum from 0

for i in range(1, n + 1):  # loop from 1 to n
    sum = sum + i           # add each number to sum

print("Sum =", sum)
