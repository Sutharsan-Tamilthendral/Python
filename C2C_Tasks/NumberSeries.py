def numberseries2():
    n = int(input("Enter the range: "))
    a = 1
    for i in range(0, n):
        a = i+a
        print(a)


def numberseries3():
    n = int(input("Enter the range: "))
    for i in range(1, n):
        print((i**3)+1)


def numberseries4():
    n = int(input("Enter the range: "))
    for i in range(n):
        print(2**i)


# numberseries2()
# numberseries3()
# numberseries4()


def decimaltobinary():
    n = int(input("Enter decimal number: "))
    ans = ""
    while n > 0:
        a = n%2
        n //= 2
        ans += str(a)

    ans = ans[::-1]
    print(ans)

# decimaltobinary()
