from typing import List

def distributeCandies(candyType: List[int]) -> int:
    return min(len(candyType)//2, len(uniqueCandyTypes(candyType)))

def uniqueCandyTypes(candyList):
    processCandyList(candyList)