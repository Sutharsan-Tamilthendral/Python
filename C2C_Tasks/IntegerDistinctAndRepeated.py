n1 = int(input())
digits = []         # [5, 4, 2, 2, 1]
repeated = []
distinct = []

while n1 > 0:
    digits.append(n1%10)
    n1//=10

for i in digits:
    check = digits.count(i)
    if check > 1:
        if repeated.count(i) == 0:
            repeated.append(i)
    elif check == 1:
        if distinct.count(i) == 0:
            distinct.append(i)

print(f"Repeated elements are {repeated}")
print(f"Distinct elements are {distinct}")