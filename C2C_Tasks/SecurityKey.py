num = int(input("Enter the number:")).__str__()
n = []
result = []

def securitykey(num):

    for i in num:
        n.append(i)

    for ele in n:
        check = n.count(ele)
        if check > 1:
            if result.count(ele) == 0:
                result.append(ele)

    print("The Security Key is ", len(result))


securitykey(num)
