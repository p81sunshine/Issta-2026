import collections

def k_similarity(s1: str, s2: str) -> int:
    deque = collections.deque([s1])
    seen = set()
    answ = 0
    
    while deque:
        for _ in range(len(deque)):
            string = deque.popleft()
            if string == s2:
                return answ
            i = 0
            while string[i] == s2[i]:
                i += 1
            for j in range(i + 1, len(string)):
                if string[i] == s2[j] != s1[j]:
                    new = string[:i] + string[j] + string[i+1:j] + string[i] + string[j+1:]
                    if new not in seen:
                        seen.add(new)
                        deque.append(new)
        answ += 1