from collections import defaultdict, deque

def isTransformable(s: str, t: str) -> bool:
    idx = defaultdict(deque)
    for i, c in enumerate(s):
        idx[int(c)].append(i)
    for c in t:
        d = int(c)
        if not idx[d]:
            return False
    idx[d].remove()
    return True