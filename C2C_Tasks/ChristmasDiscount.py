num = int(input("Enter the number: ")).__str__()
odd = []
even = []
n = []
for i in num:
    a = int(i)
    n.append(a)

for ele in n:
    if ele % 2 == 0:
        even.append(ele)
    else:
        odd.append(ele)

result = sum(odd)*sum(even)
print(result)