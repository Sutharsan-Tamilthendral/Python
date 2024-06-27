from math import *


class c2cTasks:

    def oddevenonlinegame(self, n):
        n = int(input("Enter number of elements:"))
        a = []
        even = []
        odd = []

        for i in range(0, n):
            elements = int(input(f"Enter {i} element: "))
            a.append(elements)

        for i in range(0, n):
            if a[i] % 2 == 0:
                # even_ele = a[i]
                even.append(a[i])
            else:
                # odd_ele = a[i]
                odd.append(a[i])

        result = even + odd
        print(result)

    def printsortedoddeven(self, n):
        n = int(input("Enter number elements:"))
        a = []
        even = []
        odd = []

        for i in range(0, n):
            elements = int(input(f"Enter {i} element: "))
            a.append(elements)

        for i in range(0, n):
            if a[i] % 2 == 0:
                # even_ele = a[i]
                even.append(a[i])
            else:
                # odd_ele = a[i]
                odd.append(a[i])

        for i in range(len(even)):
            for j in range(0, len(even) - i - 1):
                if even[j] > even[j + 1]:
                    even[j], even[j + 1] = even[j + 1], even[j]

        for i in range(len(odd)):
            for j in range(0, len(odd) - i - 1):
                if odd[j] > odd[j + 1]:
                    odd[j], odd[j + 1] = odd[j + 1], odd[j]

        result = even + odd
        print(result)

    def repeatdigituntilsingle(self, n):
        n = int(input("Enter number: ")).__str__()
        nums = []
        repeat = []
        distinct = []

        for i in n:
            a = int(i)
            nums.append(a)

        for i in nums:
            check = nums.count(i)
            if check > 1:
                if repeat.count(i) == 0:
                    repeat.append(i)
            elif check <= 1:
                print(f"{i} occurs only one time")

        product = prod(repeat)

        if product < 10:
            print(product)
        else:
            while product >= 10:
                ans = 0
                while product > 0:
                    ans += product % 10
                    product //= 10
                product = ans

            print(product)

    def distinctandrepeatedcount(self, n):
        n = input("Enter string or number: ")
        repeated = []
        distinct = []

        for i in n:
            check = n.count(i)
            if check > 1:
                if repeated.count(i) == 0:
                    repeated.append(i)
            elif check == 1:
                if distinct.count(i) == 0:
                    distinct.append(i)

        print(f"Repeated elements are {repeated}")
        print(f"Distinct elements are {distinct}")

    def printwithoutloop(self, n, a):
        if a == 0:
            print(a)
        elif n == a:
            print(n)
        else:
            print(n)
            n = n + 1
            self.printwithoutloop(n, a)


c2cTasks_obj = c2cTasks()

choice = int(input("What do you want to do? \n1. Print Odd and Even numbers\n"
                   "2. Print Odd and Even in sorted format\n"
                   "3. Print repeated digits until become single digit\n"
                   "4. Print the count of repeated and distinct elements\n"
                   "5. Print up to n numbers without using loop\n"
                   "Enter your choice: "))

match choice:
    case 1:
        c2cTasks_obj.oddevenonlinegame(1)
        # break

    case 2:
        c2cTasks_obj.printsortedoddeven(1)
        # break

    case 3:
        c2cTasks_obj.repeatdigituntilsingle(0)
        # break

    case 4:
        c2cTasks_obj.distinctandrepeatedcount(1)
        # break

    case 5:
        a = int(input("Where to stop: "))
        c2cTasks_obj.printwithoutloop(1, a)
        # break

    case invalid:
        print(f"Please choose valid option, there is no option for {choice}")
