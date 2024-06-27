n = int(input("Enter number elements:"))
a = []
even = []
odd = []


for i in range(0, n):
    elements = int(input(f"Enter {i} element: "))
    a.append(elements)

for i in range(0, n):
    if a[i] % 2 == 0:
        even.append(a[i])
    else:
        odd.append(a[i])

for i in range(len(even)):
    for j in range(0, len(even) - i - 1):
        if even[j] > even[j + 1]:
            even[j], even[j + 1] = even[j + 1], even[j]

for i in range(len(odd)):
    for j in range(0, len(odd) - i - 1):
        if odd[j] > odd[j + 1]:
            odd[j], odd[j + 1] = odd[j + 1], odd[j]

result = even + odd
print(result)
