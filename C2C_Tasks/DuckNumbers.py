def ducknumber(n):
    while n > 0:
        duck = n % 10
        if duck == 0:
            print("duck")
            break
        else:
            n //= 10

    if duck != 0:
        print(duck)
        print("No duck")


n = int(input("Enter the number: "))
ducknumber(n)
