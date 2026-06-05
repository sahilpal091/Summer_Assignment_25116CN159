# Q5: Sum of digits of a number

n = int(input("Enter a number: "))

sum = 0   # start sum from 0

while n > 0:           # loop until number becomes 0
    digit = n % 10     # get last digit
    sum = sum + digit  # add digit to sum
    n = n // 10        # remove last digit

print("Sum of digits =", sum)