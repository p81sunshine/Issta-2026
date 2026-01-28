import random
from typing import List

def __init__(radius: float, x_center: float, y_center: float):
    x = x_center
    y = y_center
    r = radius

def randPoint() -> List[float]:
    while True:
        x_val = random.uniform(x - r[1], x + r[1])
        y_val = random.uniform(y - r[1], y + r[1])
        if (x_val - x) ** 2 + (y_val - y) ** 2 <= r[1] ** 2:
            return [x_val, y_val]

# To use:
# rand_point_func = __init__(radius, x_center, y_center)
# param_1 = rand_point_func()