from collections import defaultdict

def get_max_repetitions(s1: str, n1: int, s2: str, n2: int) -> int:
    rec, track = [0], defaultdict(int)
    ct = start = ptr1 = ptr2 = 0

    if not set(s2).issubset(set(s1)):
        return 0

    s1 = ''.join(char for char in s1 if char in set(s2))
    
    while True:
        for char in s2:
            ptr = s1.find(char, start)
            if ptr == -1:
                ct += 1
                ptr = s1.find(char)
            start = ptr + 1
        rec.append(ct + 1)

        if rec[-1] >= n1:
            return (len(rec) - 2) // n2

        if ptr not in track:
            track[ptr] = len(rec) - 1
        
        else: 
            break
    
    cycleStart = rec[track[ptr]]
    cycle1, cycle2 = ct + 1 - cycleStart, len(rec) - 1 - track[ptr]
    rest = n1 - cycleStart
    
    rem = cycleStart + rest % cycle1

    while rec[ptr2] <= rem: 
        ptr2 += 1

    return (cycle2 * (rest // cycle1) + ptr2 - 2) // n2