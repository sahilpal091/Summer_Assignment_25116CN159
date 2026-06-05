# Q7: Product of digits of a number

n = int(input("Enter a number: "))

product = 1    # start product from 1 (not 0!)

while n > 0:               # loop until number becomes 0
    digit = n % 10         # get last digit
    product = product * digit  # multiply digit
    n = n // 10            # remove last digit

print("Product of digits =", product)