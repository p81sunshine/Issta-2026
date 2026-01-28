from functools import cache
from collections import Counter

@cache
def isScramble(s1: str, s2: str) -> bool:
    if Counter(s1) != Counter(s2):
        return False
    if s1 == s2:
        return True
    for k in range(1, len(s1)):
        if (
            isScramble(s1[:-k], s2[:-k]) and isScramble(s1[k:], s2[k:])
        ) or (
            isScramble(s1[:-k], s2[k:]) and isScramble(s1[k:], s2[:-k])
        ):
            return True
    return False