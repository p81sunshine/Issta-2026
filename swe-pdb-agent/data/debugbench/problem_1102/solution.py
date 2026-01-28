def longestWPI(A):
    curr, ans, D = 0, 0, {}
    for e, i in enumerate(map(lambda x: (-1, 1)[x > 8], A)):
        curr += i
        D[curr] = D.get(curr, e)
        ans = e + 1 if curr > 0 else max(ans, e - D.get(curr - 2, e))
    return ans