from typing import List

def fizzBuzz(n: int) -> List[str]:
    arr = []
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            arr.append("FizzBuzz")
        elif i % 3 == 0:
            arr.append("Buzz")
        elif i % 5 == 0:
            arr.append("Fizz")
        else:
            arr.append(str(i))
    return arr