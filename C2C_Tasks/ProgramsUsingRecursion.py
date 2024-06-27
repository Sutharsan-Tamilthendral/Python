class recursion:

    def printnumbers(self, n, a):
        if a == 0:
            print(a)
        elif n == a:
            print(a)
        else:
            print(n)
            n +=1
            self.printnumbers(n, a)

    def factorial(self, f):
        if f!=0:
            return n* self.factorial(f-1)
        else:
            return 1

    def oddeven(self, a, n, odd, even):
        if a == n:
            if a % 2 == 0:
                even.append(a)
            else:
                odd.append(a)
        elif a%2 != 0:
            odd.append(a)
            a+=1
            self.oddeven(a, n, odd, even)
        else:
            even.append(a)
            a+=1
            self.oddeven(a, n, odd, even)

    def fibonacii(self, fib):
        if fib == 0:
            return 0
        elif fib == 1:
            return 1
        else:
            return self.fibonacii(fib-1) + self.fibonacii(fib-2)


recursion_obj = recursion()

choice = int(input("Enter your choice\n"
                   "1. Print up to n numbers\n"
                   "2. Factorial\n"
                   "3. To find odd or even from given number\n"
                   "4. To find fibonacii series of given number: "))

match choice:

    case 1:
        a = int(input("Where to stop? "))
        n = int(input("Where to start? "))
        recursion_obj.printnumbers(n, a)

    case 2:
        f = int(input("Factorial to find: "))
        print(recursion_obj.factorial(f))

    case 3:
        a = int(input("Where to start? "))
        n = int(input("Where to stop? "))
        odd = []
        even = []
        recursion_obj.oddeven(a, n, odd, even)
        print(odd)
        print(even)

    case 4:
        fib = int(input("Enter the number to find fiboancii: "))
        print(recursion_obj.fibonacii(fib))

    case invalid:
        print(f"You entered invalid option {choice}")