def minimumPartition(s: str, k: int) -> int:
    curr, ans = 0, 1
    for d in s:
        if int(d) > k:
            return -1
        curr = 10 * curr + int(d)
        if curr > k:
            ans += 1
            curr = int(d)
    return curr