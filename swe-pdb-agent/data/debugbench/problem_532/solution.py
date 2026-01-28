from typing import List

def flipgame(fronts: List[int], backs: List[int]) -> int:
    bad = set(i for i, j in zip(fronts, backs) if i == j)
    for i in sorted(set(fronts) - set(backs)):
        if i in bad:
            continue
        return i
    return 0