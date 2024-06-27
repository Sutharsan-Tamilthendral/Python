strings = input("Enter string: ")
vowels_list = ["a", "e", "i", "o", "u"]
vowels = []
for i in strings:
    if i in vowels_list:
        if vowels.count(i) == 0:
            vowels.append(i)

print(f"The vowels in given string are {vowels}")

for ele in vowels:
    if ele in strings:
        print(f"{ele} repeated {strings.count(ele)} times in given string")