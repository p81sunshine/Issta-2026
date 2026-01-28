def find_Rotations(s): 
    n = len(s)
    s += s
    for i in range(1, n + 1):
        if s[i: i + n] == s[0: n-1]:
            return i
    return n