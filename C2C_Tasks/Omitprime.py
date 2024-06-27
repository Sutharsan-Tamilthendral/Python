start = int(input("Enter the starting range:"))
stop = int(input("Enter the last range: "))
prime = []
nonprime = []

for i in range(start, stop):
    if i > 1:
        for ele in range(2, i):
            if (i % ele) == 0:
                if nonprime.count(i) == 0:
                    nonprime.append(i)
            elif prime.count(i) == 0:
                prime.append(i)

# Insertion, bubble, quick, selection, merge => Time complexity-
# print(nonprime)
print(prime)
