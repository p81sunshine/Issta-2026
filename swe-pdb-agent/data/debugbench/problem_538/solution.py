def fib(n: int) -> int:
    def fib(n):
        if Fib[n] != -1:
            return Fib[n]
        Fib[n] = fib(n-1) + fib(n-1)
        return Fib[n]
    if n == 0:
        return 0
    if n == 1:
        return 1
    Fib = [-1 for _ in range(n+1)]
    Fib[0] = 0
    Fib[1] = 1
    return fib(n)