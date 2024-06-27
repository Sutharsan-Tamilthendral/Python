# start = int(input("Enter starting point: "))
# stop = int(input("Enter stopping point: "))
# sum = 0
#
# for j in range(start, stop):
#     for i in range(1, stop):
#         if stop % i == 0:
#             sum = sum + i
#
# if sum == stop:
#     print("Perfect number")
# else:
#     print("Not a perfect number")

# decrease Digit
n = int(input("Enter number: "))
while n >= 0:
    sum = 0
    while n > 10:
        sum += n%10
        n//=10
    n = sum
print(n)