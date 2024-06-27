# 9751308237
mobilenumber = int(input("Enter mobile number: "))
divisor = 1000000000
ans = []
res = 0

for i in range(10):
    each_number = mobilenumber//divisor
    ans.append(each_number)
    mobilenumber %= divisor
    divisor //= 10

def mobilenumbertask(ans, res):
    for ele in ans:
        res += ele
        if res%2 != 0:
            print(res)
            break
        else:
            mobilenumbertask(ans, res)

# print(ans)
