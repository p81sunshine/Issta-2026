from solution import *

def test_example_1():
    grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
    assert numMagicSquaresInside(grid) == 1, "First example should return 1"

def test_example_2():
    grid = [[8]]
    assert numMagicSquaresInside(grid) == 0, "Grid too small should return 0"

def test_magic_square_needs_reversal():
    grid = [[7,5,3],[2,9,4],[6,1,8]]
    assert numMagicSquaresInside(grid) == 1, "Reversed magic square should be counted"

def test_non_magic_square():
    grid = [[1,1,1],[1,1,1],[1,1,1]]
    assert numMagicSquaresInside(grid) == 0, "All 1s grid should not be magic square"

def test_valid_magic_square():
    grid = [[2,7,6],[9,5,1],[4,3,8]]
    assert numMagicSquaresInside(grid) == 1, "Direct match to solution should return 1"