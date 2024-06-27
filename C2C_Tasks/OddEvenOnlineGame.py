n = int(input("Enter number elements:"))
a = []
even = []
odd = []

def sortedoddeven(n):
    for i in range(0, n):
        elements = int(input(f"Enter {i} element: "))
        a.append(elements)

    for i in range(0, n):
        if a[i] % 2 == 0:
            even.append(a[i])
        else:
            odd.append(a[i])

    result = sorted(even)+sorted(odd)
    print(result)

sortedoddeven(n)