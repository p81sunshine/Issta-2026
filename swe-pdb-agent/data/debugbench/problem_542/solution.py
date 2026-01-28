from typing import List

def stoneGameVI(a: List[int], b: List[int]) -> int:
    combines = [(a[i] + c[i], a[i], b[i]) for i in range(len(a))]
    combines.sort(reverse=True)
    bobPoints = sum(b)
    alicePoints = 0
    for i in range(0, len(a), 2):
        alicePoints += combines[i][1]
        bobPoints -= combines[i][2]
    if alicePoints > bobPoints:
        return 1
    elif alicePoints < bobPoints:
        return -1
    return 0