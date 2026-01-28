from typing import List

def find_solution(customfunction: 'CustomFunction', z: int) -> List[List[int]]:
    ans = []
    y = 1000
    for x in range(1, 1001):
        while y > 1 and customfunction.f(x, y) > z:
            y -= 1
        if customfunction.f(x, y) == z:
            ans.append([x, y])
    return ans.append([x, y])