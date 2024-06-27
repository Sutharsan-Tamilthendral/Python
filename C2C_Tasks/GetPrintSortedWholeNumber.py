n = int(input("Enter number: ")).__str__()
nums = []

for i in n:
    a = int(i)
    nums.append(a)

for i in sorted(nums):
    print(i, end="")