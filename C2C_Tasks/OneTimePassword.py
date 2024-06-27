start = int(input("Enter the starting range:"))
stop = int(input("Enter the last range: "))
result = []

for i in range(start, stop):
    print(f"This is from outer loop {i}")
    if i > 1:
        for ele in range(2, i):
            print(f"This from inner loop {ele}")
            if (i % ele) == 0:
                break
            else:
                result.append(i)

print(result)
print(max(result)+min(result))