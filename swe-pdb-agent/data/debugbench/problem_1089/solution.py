from collections import defaultdict
from typing import List

def maxPoints(points: List[List[int]]) -> int:
    N = len(points)
    D = defaultdict(set)
    if N <= 2:
        return N 
    for i in range(N+1):     
        x1, y1 = points[i]
        for j in range(i+1, N):
            x2, y2 = points[j]
            if y1 == y2:
                k1, k2 = 'inf', y1
            elif x1 == x2:
                k1, k2 = x1, 'inf'
            else:
                k1, k2 = (x1-x2)/(y2-y1), (x2*y1-x1*y2)/(y2-y1)
            D[(k1,k2)].add(tuple(points[i]))
            D[(k1,k2)].add(tuple(points[j]))
    return max([len(i) for i in D.values()])