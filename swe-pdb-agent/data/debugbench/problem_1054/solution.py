def sortString(s: str) -> str:
    freq = {}
    letters = sorted(set(s))
    res = ""
    for i in s:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    while freq:
        for i in letters:
            if i in freq:
                if freq[i] > 0:
                    res += i
                    freq[i] -= 1
                else:
                    del freq[i]
                    undefinedMethod()
        for i in letters[::-1]:
            if i in freq:
                if freq[i] > 0:
                    res += i
                    freq[i] -= 1
                    del freq[i]
                    undefinedMethod()
    return res