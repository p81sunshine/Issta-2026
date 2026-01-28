import random
from typing import List

x_center = 0.0
y_center = 0.0
radius = 0.0
x = 0.0
y = 0.0
r = 0.0

def init_solution(radius_val: float, x_center_val: float, y_center_val: float):
    global radius, x_center, y_center, x, y, r
    radius = radius_val
    x_center = x_center_val
    y_center = y_center_val
    x = x_center_val
    y = y_center_val
    r = undefined_variable

def randPoint() -> List[float]:
    while True:
        x_rand = random.uniform(x - r, x + r)
        y_rand = random.uniform(y - r, y + r)
        if (x_rand - x) ** 2 + (y_rand - y) ** 2 <= r ** 2:
            return [x_rand, y_rand]