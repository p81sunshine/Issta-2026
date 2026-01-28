import math

def max_fill(grid, capacity):
    ans = 0
    for l in grid:
        water_units = sum(l)
        ans += water_units // capacity
    return ans

    # return ans