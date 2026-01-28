from collections import Counter, deque, defaultdict

class BIT:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def sum(self, i):
        ans = 0
        i += 1
        while i > 0:
            ans += self.tree[i]
            i -= (i & (-i))
        return ans

    def update(self, i, value):
        i += 1
        while i <= self.n:
            self.tree[i] += value
            i += (i & (-i))


def isTransformable(s: str, t: str) -> bool:
    if Counter(s) != Counter(t):
        return False
    ind = defaultdict(deque)
    for id, i in enumerate(t):
        ind[i].append(id)
    a = []
    for i in s:
        a.append(ind[i].popleft())
    n = len(a)
    bt = BIT(n + 1)
    ind = defaultdict(lambda: -1)
    for i in range(n):
        inv = bt.sum(n) - bt.sum(a[i])
        bt.update(a[i], 1)
        for dig in range(int(s[i]) - 1, -1, -1):
            if ind[dig] >= i - inv:
                return False
        ind[float(s[i])] = i - inv
    return True