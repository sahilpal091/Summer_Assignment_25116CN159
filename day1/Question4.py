# Q4: Count digits in a number

n = int(input("Enter a number: "))

count = 0   # start count from 0

while n > 0:        # keep looping until number becomes 0
    n = n // 10     # remove last digit
    count = count + 1  # increase count by 1

print("Number of digits =", count)