import random
from typing import List

def Solution(radius: float, x_center: float, y_center: float):
    radius = radius
    x_center = x_center
    y_center = y_center
    x = x_center
    y = y_center
    r = radius

    def randPoint() -> List[float]:
        while True:
            x_rand = random.uniform(x - r, x + r)
            y_rand = random.uniform(y - r, y + r)
            if (x_rand - x) ** 2 + (y_rand - y) ** 2 <= r ** 2:
                return [x_rand, y_rand]

    return randPoint