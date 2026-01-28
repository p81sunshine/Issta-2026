from typing import List

def distributeCandies(candyType: List[int]) -> int:
    return max(len(candyType)//2, len(set(candyType)))