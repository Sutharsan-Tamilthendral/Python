# from threading import *
# from time import *
#
# class Hello(Thread):
#
#     def run(self):
#         for i in range(5):
#             print("HELLO")
#             sleep(1)
#
# class Hi(Thread):
#     def run(self):
#         for i in range(5):
#             print("HI")
#             sleep(1)
#
#
# t1 = Hello()
# t2 = Hi()
#
# t1.start()
# sleep(0.2)
# t2.start()
#
# t1.join()
# t2.join()
#
# if t1.is_alive():
#     print("The t1 is alive")
#
# print("Sutharsan")

# try:
#     a = int(input("Enter integer "))
#     print(a)
# except Exception:
#     print("Enter integer value you have entered string")
# import heapq
# def find_even(even):
#     return even%2 == 0
#
# even = [5,7,2,1,4,6,9,10,8]
# Syntax: filter(function, sequence)
# even_nums = filter(find_even, even)
# print(list(even_nums))
# all_function = all(ele%2 == 0 for ele in even_nums)
# print(all_function)
# any_function = any(ele < 20 for ele in list(even_nums))
# print(any_function)
# str1 = "Sutharsan"
# print(hash(str1))
# print(heapq.nlargest(2, even)[-1])
# print(heapq.nsmallest(3, even))

def generate_series(n):
    series = []
    total = 0
    for i in range(1, n+1):
        total += i
        if total <= n:
            series.append(total)
    return series

# print(generate_series(50))

def generate_series_b(n):
    series = []
    num = 1
    for i in range(n):
        series.append(int(str(num) + str(num+1) + str(num+2)))
        num += 1
    return series

# n = int(input("Enter the number of terms: "))
# print(generate_series_b(n))

def reverse_number(n):
    reversed_num = 0
    swaps = 0

    while n > 0:
        rem = n % 10
        reversed_num = reversed_num * 10 + rem
        n = n // 10
        swaps += 1
    return reversed_num, swaps

n = int(input("Enter a positive number: "))
reversed_num, swaps = reverse_number(n)
print(f"Reversed number: {reversed_num}")
print(f"Number of swaps: {swaps}")