s = input("Enter the string:")
need = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
check = []

for i in s:
    check.append(i)

print("The Secret Message is ", end="")

for ele in check:
    if ele in need:
        print(ele, end="")
