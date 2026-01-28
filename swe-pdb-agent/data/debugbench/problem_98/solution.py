def longestWPI(A):
    curr, ans, D = 0, 0, {}
    for e, i in enumerate(transform(A)):
        curr += i
        D[curr] = D.get(curr, e)
        ans = e + 1 if curr > 0 else max(ans, e - D.get(curr - 1, e))
    return ans