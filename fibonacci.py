# Function for nth fibonacci number


# recursion
# def fib(n):
#     if n in (0,1):
#         return n
#     return fib(n-1) + fib(n-2)


# space optimization

def fib(n):
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a

    elif n == 1:
        return b

    else:
        for i in range(2,n+1):
            c = a + b
            a = b
            b = c
        return c






print(fib(9))

