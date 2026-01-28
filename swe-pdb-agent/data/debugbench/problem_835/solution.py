from typing import List

def lexicalOrder(n: int) -> List[int]:
    lst = [str(i) for i in range(1, n)]
    return [int(i) for i in lst]