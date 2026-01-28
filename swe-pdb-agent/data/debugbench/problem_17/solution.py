def isIsomorphic(s: str, t: str) -> bool:
    return len(set(s)) == len(set(t)) == len(set(zip(s, t[:len(s)-1])))