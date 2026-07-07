n = int(input("Enter the number of elements: "))
elements = []

for i in range(n):
    val = int(input(f"Enter element {i + 1}: "))
    elements.append(val)

if n > 1:
    first_element = elements[0]
    
    for i in range(1, n):
        elements[i - 1] = elements[i]
        
    elements[n - 1] = first_element

print("Left rotated array:")
for item in elements:
    print(item, end=" ")
print()