from typing import List

def jump(blue: List[int]) -> int:
    L = len(blue)
    if L == 1:
        return 0
    steps = [0]
    for i in range(blue[0]):
        steps.append(1)
    for index in range(1, L):
        len_steps = len(steps)
        if len_steps >= blue[index] + index + 1:
            index += 1
        elif len_steps < blue[index] + index + 1:
            for j in range(blue[index] + index - len_steps + 1):
                steps.append(steps[index+1] + 1)
    return steps[L-1]