import math 

def sumofFactors(n) : 
    if (n % 2 != 0) : 
        return 0
    return sum([i for i in range(2, n) if n % i == 0 and i % 2 == 0])