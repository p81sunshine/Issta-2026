from typing import List

def restoreIpAddresses(s: str) -> List[str]:
    res = []
    cur = []
    def backtrack(i):
        if i == len(s) and len(cur) == 4:
            res.append(".".join(cur))
            return
        if len(cur) > 4 or i > len(s):
            return
        if s[i] == '0':
            cur.append(s[i])
            backtrack(i+1)
            cur.pop()
            return
        j = 0
        while j < 4 and i + j < len(s):
            if int(s[i:i+j+1]) < 256:
                cur.append(s[i:i+j+1])
                backtrack(i + j + 1)
                cur.pop()
            j += 1
    backtrack(0)
    return res