def memoize(func):
    cache = {}
    def inner(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return inner

@memoize
def fib(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    return fib(n-2) + fib(n-1)
