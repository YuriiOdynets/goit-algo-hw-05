def caching_fibonacci ():
    cache = {}
    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            return cache[n]
        
        cache[n] = fibonacci(n-1) + fibonacci(n-2)
        #Додатковий принт просто що можна включити для наглядності роботи кешу
        print(f"Cache after calculating fibonacci({n}):", cache)
        return cache[n]
    return(fibonacci)

fib = caching_fibonacci()


print(fib(15))

print(fib(16))

print(fib(12))