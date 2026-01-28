from typing import List
from collections import defaultdict

def findWinners(matches: List[List[int]]) -> List[List[int]]:

    winners, losers = defaultdict(int), defaultdict(int)

    for match in matches:

        winners[match[0]] += 1
        losers[match[2]] += 1

    res_1, res_2 = [], []

    for k, v in winners.items():
        if k not in losers:
            res_1.append(k)
    
    for k, v in losers.items():
        if v == 1:
            res_2.append(k)

    res_1.sort()
    res_2.sort()
    
    return [ res_1, res_2 ]