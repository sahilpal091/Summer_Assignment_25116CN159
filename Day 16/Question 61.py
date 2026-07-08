# Program to find missing number in array
# Array contains numbers from 1 to n with one missing

def find_missing_number(arr, n):
    # Sum of first n natural numbers
    total_sum = n * (n + 1) // 2

    # Sum of elements present in array
    arr_sum = 0
    for i in range(len(arr)):
        arr_sum = arr_sum + arr[i]

    # Missing number = expected sum - actual sum
    missing = total_sum - arr_sum
    return missing


# Main program
n = 8  # numbers from 1 to 8
arr = [1, 2, 4, 5, 6, 7, 8]  # 3 is missing

result = find_missing_number(arr, n)
print("The missing number is:", result)