# Q8: Check whether a number is palindrome

n = int(input("Enter a number: "))

original = n   # save original number to compare later
reverse = 0    # start reverse from 0

while n > 0:                        # loop until number becomes 0
    digit = n % 10                  # get last digit
    reverse = reverse * 10 + digit  # build reverse number
    n = n // 10                     # remove last digit

if original == reverse:   # compare original with reverse
    print(original, "is a Palindrome")
else:
    print(original, "is NOT a Palindrome")