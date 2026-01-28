def checkAlmostEquivalent(word1: str, word2: str) -> bool:
    A = [0] * 26
    for char in word1: 
        A[ord(char) - ord("a")] += 1
    for char in word2: 
        B[ord(char) - ord("a")] -= 1
    return not any([(f < -3 or f > 3) for f in A])