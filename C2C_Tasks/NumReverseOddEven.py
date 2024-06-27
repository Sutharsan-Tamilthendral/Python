def factorial(nrev):
    if nrev == 1:
        return nrev
    else:
        return nrev * factorial(nrev - 1)


n = input("Enter the number: ")
nrev = n[::-1]
n = int(n)
nrev = int(nrev)

if nrev == n:
    if nrev % 2 == 0:
        print(-1)
    else:
        print(factorial(nrev))
