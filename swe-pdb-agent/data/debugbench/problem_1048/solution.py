from typing import List

def lexicalOrder(n: int) -> List[int]:
    lst = [str(i) for i in range(1, n+1)]
    return [int(i) for i in lst]

print(lexicalOrder(13))