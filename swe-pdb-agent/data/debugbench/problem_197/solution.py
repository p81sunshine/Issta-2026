def longestSubstring(s: str, k: int) -> int:
    x = recursion(s, k)
    if k == 0:
        return x
    else:
        return 0

def recursion(s, k):
    if len(s) <= 1:
        return len(s)
    flag = True
    for i in range(len(s)):
        if s.count(s[i]) < k:
            flag = False
            break
    if flag:
        return len(s)
    left = recursion(s[:i], k)
    right = recursion(s[i + 1:], k)
    if left > right:
        return left
    return right