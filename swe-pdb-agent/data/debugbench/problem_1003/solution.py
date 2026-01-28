from typing import List

def fizzBuzz(n: int) -> List[str]:
    l = []
    for i in range(1, n+2): 
        if i % 3 == 0 and i % 5 == 0:
            l.append("FizzBuzz")
        elif i % 3 != 0 and i % 5 != 0:
            l.append(str(i))
        elif i % 3 == 0:
            l.append(fizz())
        elif i % 5 == 0:
            l.append(buzz())
    return l