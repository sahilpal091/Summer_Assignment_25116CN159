n = int(input("Enter the number of elements: "))
elements = []

for i in range(n):
    val = int(input(f"Enter element {i + 1}: "))
    elements.append(val)

start = 0
end = n - 1

while start < end:
    temp = elements[start]
    elements[start] = elements[end]
    elements[end] = temp
    start = start + 1
    end = end - 1

print("Reversed array:")
for item in elements:
    print(item, end=" ")
print()