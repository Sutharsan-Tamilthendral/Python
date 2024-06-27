a = int(input())
b = int(input())
c = int(input())

if (a<b) and (a<c):
    print(b+c)
elif (b<c) and (b<a):
    print(a+c)
else:
    print(a+b)