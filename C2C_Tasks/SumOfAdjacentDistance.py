n = int(input("Enter number of element:"))
a = []
b = []

def sumofadjacentnumbers(n):
    for i in range(0, n):
        element = int(input())
        a.append(element)

    length = len(a)

    for i in range(0, length-1):
        ele = a[i]
        i += 1
        ele1 = a[i]
        ele2 = ele-ele1
        # if ele2 < 0:
        #     ele2 *= -1
        b.append(ele2)

    print("The sum of adjacent distance is", sum(b))


sumofadjacentnumbers(n)
