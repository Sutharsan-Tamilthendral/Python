from math import *

n = int(input("Enter number: ")).__str__()
nums = []
repeat = []
distinct = []

for i in n:
    a = int(i)
    nums.append(a)

for i in nums:
    check = nums.count(i)
    if check > 1:
        if repeat.count(i) == 0:
            repeat.append(i)
    elif check <= 1:
        print(f"{i} occurs only one time")

product = prod(repeat)
print(product)

if product < 10:
    print(product)
else:
    while product >= 10:
        ans = 0
        while product > 0:
            ans += product % 10
            product //= 10
        product = ans

    print(product)