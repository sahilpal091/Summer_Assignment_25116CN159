def is_armstrong(num):
    temp = num
    digits_count = 0
    
    while temp > 0:
        digits_count = digits_count + 1
        temp = temp // 10
        
    temp = num
    total_sum = 0
    
    while temp > 0:
        remainder = temp % 10
        total_sum = total_sum + (remainder ** digits_count)
        temp = temp // 10
        
    if total_sum == num:
        return True
    else:
        return False

number = int(input("Enter a number: "))

if is_armstrong(number):
    print("The number is an Armstrong number")
else:
    print("The number is NOT an Armstrong number")