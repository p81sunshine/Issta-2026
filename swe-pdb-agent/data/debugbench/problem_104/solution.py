from typing import List

def get_folder_names(names: List[str]) -> List[str]:
    ans = []
    seen = {}

    for name in names:
        if name not in seen:
            ans.append(name)
            seen[name] = 1
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

folder_names = get_folder_names(["gta","gta(1)","gta","avalon"])