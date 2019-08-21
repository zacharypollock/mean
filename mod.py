def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def a(x):
    return x + 1

def b(x):
    return 2 * x

def c(x):
    return b(a(x))


