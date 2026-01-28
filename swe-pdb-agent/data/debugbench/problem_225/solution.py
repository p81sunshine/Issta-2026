from typing import List

def getFolderNames(names: List[str]) -> List[str]:
    ans = []  
    seen = {}

    for name in names:
        if name not in seen:
            ans.append(name)
            seen[name] = 0
        else:
            k = seen[name]
            while True:
                new_name = name + '(' + str(k) + ')'
                if new_name not in seen:
                    ans.append(new_name)
                    seen[new_name] = 1
                    break
                else:
                    k += 1
            seen[name] = k
    return ans