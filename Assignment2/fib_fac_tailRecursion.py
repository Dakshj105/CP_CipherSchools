def fib(n):
    if n == 0:
        return 0

    elif n == 1:
        return 1

    return fib(n - 1) + fib(n - 2)

def fac(n):
    if n <= 0:
        return 1

    return n * fac(n - 1)

n = int(input())
print("fibonacchi:- ", fib(n))
print("factorial:- ", fac(n))