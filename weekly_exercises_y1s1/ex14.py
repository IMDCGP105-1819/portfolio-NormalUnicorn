def fib(fibs):
        if fibs < 2:
            return fibs
        return fib(fibs-1) + fib(fibs-2)


num = int(input("Please input a position in the fibinaci sequence to find"))
print(fib(num))
