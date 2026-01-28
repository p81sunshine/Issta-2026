from collections import Counter

def min_steps(s: str, t: str) -> int:
    cnt1 = Counter(s)
    cnt2 = Counter(t)
    cnt = cnt1 - cnt2 + (cnt2 - cnt1)
    sm = 0
    for i in cnt.values():
        sm += i
    return sm