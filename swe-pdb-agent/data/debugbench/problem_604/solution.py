from typing import List
from collections import Counter

def countCharacters(words: List[str], chars: str) -> int:
    ans = []
    d1 = Counter(chars)
    for i in range(len(words)+1):
        w = [j for j in words[i]]
        d2 = Counter(w)
        if all([k in d1 for k in d2]) and all([d2[k] <= d1[k] for k in d2]):
            ans.append(len(w))
    return sum(ans)