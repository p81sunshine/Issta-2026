def compare_char(s, i, j):
    return s[i] == s[j]

def longest_prefix(s: str) -> str:
    n = len(s)
    lps = [0] * n
    j = 0
    for i in range(1, n):
        if not compare_char(s, i, j):
            j = lps[j]

        if s[i] == s[j]:
            lps[i] = j + 1
            j += 1

    return s[:lps[-1]]