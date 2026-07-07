arr = [12, 35, 1, 10, 34, 1]

largest = arr[0]
second_largest = -1

for i in range(1, len(arr)):
    if arr[i] > largest:
        second_largest = largest
        largest = arr[i]
    elif arr[i] > second_largest and arr[i] != largest:
        second_largest = arr[i]

print("The second largest element is:", second_largest)