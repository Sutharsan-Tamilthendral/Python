def evenorodd(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")


num = int(input("Enter number:"))
evenorodd(num)


def evenoroddbool(num1):
    if num1 % 2 == 0:
        return True
    else:
        return False


num1 = int(input("Enter number:"))
print(evenoroddbool(num1))




