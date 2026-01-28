import math
def sum(a,b): 
    sum = 0
    n = math.gcd(a, b)
    N = int(math.sqrt(n))
    for i in range (1, N): 
        if (n % i == 0): 
            sum += i
            if (n / i != i): 
                sum += (n // i)
    return sum