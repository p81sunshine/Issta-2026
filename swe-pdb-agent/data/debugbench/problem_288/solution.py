from collections import defaultdict, deque

def isTransformable(s: str, t: str) -> bool:
    idx = defaultdict(deque)
    for i, c in enumerate(s):
        idx[int(c)].append(i)
    for c in t:
        d = int(c)
        if not idx[d + 1]: 
            return False
        for i in range(d):
            if idx[i] and idx[i][0] < idx[d][0]: 
                return False
        idx[d].popleft()
    return True