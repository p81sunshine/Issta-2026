import random
from typing import List

def create_rand_point(radius: float, x_center: float, y_center: float):
    x = x_center
    y = y_center
    r = radius
    def rand_point() -> List[float]:
        while True:
            x_candidate = random.uniform(x - r, x + r)
            y_candidate = random.uniform(y - r, y + r)
            if (x_candidate - x) ** 2 + (y_candidate - y) ** 2 <= r ** 2:
                return [x_candidate, y_candidate]
    return rand_point

# Example usage:
# rand_point_func = create_rand_point(radius, x_center, y_center)
# param_1 = rand_point_func()