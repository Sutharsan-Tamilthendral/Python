def nums(n, a):
    if a == 0:
        print(a)
    elif n == a:
        print(n)
    else:
        print(n)
        n = n + 1
        nums(n, a)


a = int(input("Where to stop: "))
nums(1, a)


def factorial(f):
    if f != 0:
        return f*factorial(f-1)
    else:
        return 1

print(factorial(5))
