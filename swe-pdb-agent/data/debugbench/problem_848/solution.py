from typing import List

def maxDistance(colors: List[int]) -> int:
    ans = 0
    for i, x in enumerate(colors):
        if x == colors[0]: ans = max(ans, i)
        if x == colors[-1]: ans = max(ans, len(colors)-1-i)
    return ans