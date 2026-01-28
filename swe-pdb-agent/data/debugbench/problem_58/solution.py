from typing import List

def lexicalOrder(n: int) -> List[int]:
    lst = [str(i) for i in range(1, n+1)]
    lst.sort()
    return [int(i) for i in lst]