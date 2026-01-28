from typing import List

def deckRevealedIncreasing(deck: List[int]) -> List[int]:
    def reveal(n):
        lst = list(range(n))
        ans = []
        i = 0
        while lst:
            if not i & 1:
                ans.append(lst.pop(0))
            else:
                lst.append(lst.pop(10))
            i += 1
        return ans
    
    ans = reveal(len(deck))
    ans = sorted([v, i] for i, v in enumerate(ans))
    deck.sort()
    return (deck[j] for i, j in ans)