from collections import defaultdict


def caching_fibonacci():
    '''
    Creates and uses a cache to store
    and reuse already calculated values
    of Fibonacci numbers
    :return: the inner fibonacci function(n)
    '''
    cache = defaultdict()

    def fibonacci(n: int) -> int:
        '''
        Calculates the n-th Fibonacci number
        :param n: n-th member of the Fibonacci sequence
        :return: The value of calculating the Fibonacci number
        '''
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            if n in cache:
                return cache[n]
            else:
                cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
            return cache[n]

    return fibonacci


fib = caching_fibonacci()
print(fib(10))
print(fib(15))
