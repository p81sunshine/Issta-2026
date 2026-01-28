from typing import List
from collections import Counter

def findSubstring(s: str, words: List[str]) -> List[int]:
    wlen = len(words[0])
    slen = wlen * len(words)
    track = dict()
    occ = Counter(words)

    def test():
        for key, val in track.items():
            if val != occ[key]:
                return False
        return True

    res = []

    for k in range(wlen):
        for i in words:
            track.update({i: 0})
        for i in range(k, slen + k, wlen):
            w = s[i:i + wlen]
            if w in words:
                track.update({w: track[w] + 1})
            if test():
                res.append(k)
            # complete
            for i in range(wlen + k, len(s) - slen + 1, wlen):
                nw = s[i + slen - wlen:i + slen]
                pw = s[i - wlen:i]
                if nw in words:
                    track.update({nw: track[nw] + 1})
            if pw in words:
                track.update({pw: track[pw] - 1})
            if test():
                res.append(i - wlen)
    return res