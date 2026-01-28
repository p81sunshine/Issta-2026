import random
from typing import List

def create_solution(radius: float, x_center: float, y_center: float):
    radius = radius
    x_center = x_center
    y_center = y_center
    x = x_center
    y = y_center
    r = undefined_variable

    def rand_point() -> List[float]:
        while True:
            x_val = random.uniform(x - r, x + r)
            y_val = random.uniform(y - r, y + r)
            if (x_val - x) ** 2 + (y_val - y) ** 2 <= r ** 2:
                return [x_val, y_val]

    return rand_point

# Usage example:
# rand_point_func = create_solution(radius, x_center, y_center)
# param_1 = rand_point_func()