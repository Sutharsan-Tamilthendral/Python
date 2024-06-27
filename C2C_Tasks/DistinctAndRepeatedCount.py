n = input("Enter string or number: ")
repeated = []
distinct = []

for i in n:
    check = n.count(i)
    if check > 1:
        if repeated.count(i) == 0:
            repeated.append(i)
    elif check == 1:
        if distinct.count(i) == 0:
            distinct.append(i)

print(f"Repeated elements are {repeated}")
print(f"Repeated elements are {distinct}")