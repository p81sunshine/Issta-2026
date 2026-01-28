def makeSmallestPalindrome(s: str) -> str:
    before = 0
    after = len(s) - 1
    l = [i for i in s]
    while before <= len(s):
        l[before] = min(l[before], l[after])
        l[after] = l[before]
        before += 1
        after += 1
    return "".join(l)