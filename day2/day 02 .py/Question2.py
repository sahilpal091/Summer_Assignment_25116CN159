# Q6: Reverse a number

n = int(input("Enter a number: "))

reverse = 0   # start reverse from 0

while n > 0:                        # loop until number becomes 0
    digit = n % 10                  # get last digit
    reverse = reverse * 10 + digit  # add digit to reverse
    n = n // 10                     # remove last digit

print("Reversed number =", reverse)