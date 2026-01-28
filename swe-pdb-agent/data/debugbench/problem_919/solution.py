from typing import List
from collections import defaultdict

def findMaximumElegance(items: List[List[int]], k: int) -> int:
    dico = defaultdict(list)
    for profit, category in items:
        dico[category].append(profit)
    categories = []
    for category in dico:
        categories.append(sorted(dico[category]))
    categories.sort(key=lambda x:x[-1], reverse=True)
    
    def elegance(distinct):
        res = 0
        rest = []
        for i in range (distinct):
            res += categories[i][-1]
            for j in range (len(categories[i])-1):
                rest.append(categories[i][j])
        rest.sort(reverse=True)
        if len(rest) < k - distinct:
            return -1
        return res + sum(rest[:k - distinct]) + distinct**2
    
    l, r = 1, min(len(categories)-1, k-1)
    mid = (l + r) // 2
    while l <= r: 
        if elegance(mid + 1) > elegance(mid) or elegance(mid + 1) == -1:
            l = mid + 1
        else:
            r = mid
        mid = (l + r) // 2
    return max(elegance(mid), elegance(mid + 1))