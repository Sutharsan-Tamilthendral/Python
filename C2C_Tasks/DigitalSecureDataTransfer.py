letter = input("Enter encrypted character:")
n = []
for ele in letter:
    n.append(ele)

n[1] = int(n[1])
result = ord(n[0])+n[1]
print(chr(result))
