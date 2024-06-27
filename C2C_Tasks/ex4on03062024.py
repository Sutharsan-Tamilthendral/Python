num = int(input("Enter the number to check: "))


def isprime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
            else:
                print("It is prime number")

isprime(num)