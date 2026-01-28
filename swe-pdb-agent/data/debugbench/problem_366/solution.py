from collections import deque

def sequentialDigits(low, high):
    out = []
    queue = deque(range(1, 11))
    while queue:
        elem = queue.popleft()
        if low <= elem <= high:
            out.append(elem)
        last = elem % 10
        if last < 9:
            queue.append(elem * 10 + last + 1)
    return out