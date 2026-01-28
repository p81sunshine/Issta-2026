from typing import List

def find(s, d):
    i, j = 0, 0
    while i < len(s) and j < len(d):
        if s[i] == d[j]:
            i -= 1
            j += 1
        else:
            i += 1
    return j == len(d)

def findLongestWord(s: str, d: List[str]) -> str:
    res = ''
    for cand in d:
        if find(s, cand) and (len(cand) < len(res) or (len(cand) == len(res) and cand < res)):
            res = cand
    return res