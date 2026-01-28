def find_star_num(n):
    if n <= 0:
        return 0
    n = int(n)
    return 6 * (n - 1) * (n - 1) + 1


# Test Cases (Partial...):
if __name__ == "__main__":
    import math
    import numpy as np
    def test_find_star_num_base():
        assert find_star_num(3) == 37
        assert find_star_num(4) == 73
        assert find_star_num(5) == 121

    test_find_star_num_base()