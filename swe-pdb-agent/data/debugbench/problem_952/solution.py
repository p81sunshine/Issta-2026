from typing import List

def word_count(startWords: List[str], targetWords: List[str]) -> int:
    seen = set()
    for word in startWords: 
        m = 0
        for ch in word: 
            m ^= 1 << ord(ch)-97
        seen.add(m)
        
    ans = 0 
    for word in targetWords: 
        m = 0 
        for ch in word: 
            m ^= 1 << ord(ch)-97
        for ch in word: 
            if m ^ (1 << ord(ch)-97) not in seen: 
                ans += 1
                break 
    return ans