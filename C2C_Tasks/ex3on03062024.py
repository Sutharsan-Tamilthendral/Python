num = int(input("Enter the number: ")).__str__()
arm = []
ans = []

def armstrong(num):
    for i in num:
        a = int(i)
        arm.append(a)

    length = len(arm)
    for ele in arm:
        b = ele**length
        ans.append(b)

    num = int(num)

    if num == sum(ans):
        print("The given number is armstrong")
    else:
        print("The given number is not an armstrong")

armstrong(num)