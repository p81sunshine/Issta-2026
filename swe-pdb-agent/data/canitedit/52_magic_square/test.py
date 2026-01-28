from solution import *
import math

from typing import List

def test_all():
    def is_valid_magic_square(soln: List[List[int]], order: int) -> bool:
        magic_const = order * (order**2 + 1) // 2
        for row in soln:
            if sum(row) != magic_const:
                return False
        for col in range(order):
            if sum(soln[row][col] for row in range(order)) != magic_const:
                return False
        if sum(soln[i][i] for i in range(order)) != magic_const:
            return False
        if sum(soln[i][order - 1 - i] for i in range(order)) != magic_const:
            return False
        return True

    for order in range(3, 5):
        soln = magic_square(order)
        assert soln != "No solution exists"
        assert is_valid_magic_square(soln, order)

    # one with no solution
    assert magic_square(2) == "No solution exists"