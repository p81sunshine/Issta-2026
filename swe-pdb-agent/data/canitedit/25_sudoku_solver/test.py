from solution import *
import math

def test_all():
    def __eval_secret_check_valid(board: List[List[int]]) -> bool:
        for row in board:
            if len(set(row)) != 9:
                return False

        for col in zip(*board):
            if len(set(col)) != 9:
                return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                square = [board[x][y]
                          for x in range(i, i+3) for y in range(j, j+3)]
                if len(set(square)) != 9:
                    return False
        return True

    b1 = """0 0 0 0 9 4 0 3 0
0 0 0 5 1 0 0 0 7
0 8 9 0 0 0 0 4 0
0 0 0 0 0 0 2 0 8
0 6 0 2 0 1 0 5 0
1 0 2 0 0 0 0 0 0
0 7 0 0 0 0 5 2 0
9 0 0 0 6 5 0 0 0
0 4 0 9 7 0 0 0 0"""
    solved = solve(b1)
    assert solved is not None
    assert __eval_secret_check_valid(solved)
    assert check_valid(solved)

    b3 = """5 3 0 0 7 0 0 0 0
6 0 0 1 9 5 0 0 0
0 9 8 0 0 0 0 6 0
8 0 0 0 6 0 0 0 3
4 0 0 8 0 3 0 0 1
7 0 0 0 2 0 0 0 6
0 6 0 0 0 0 2 8 0
0 0 0 4 1 9 0 0 5
0 0 0 0 8 0 0 7 9"""
    solved = solve(b3)
    assert solved is not None
    assert __eval_secret_check_valid(solved)
    assert check_valid(solved)

    b4 = """0 0 0 0 0 0 0 0 0
0 0 0 0 0 3 0 8 5
0 0 1 0 2 0 0 0 0
0 0 0 5 0 7 0 0 0
0 0 4 0 0 0 1 0 0
0 9 0 0 0 0 0 0 0
5 0 0 0 0 0 0 7 3
0 0 2 0 1 0 0 0 0
0 0 0 0 4 0 0 0 9"""
    solved = solve(b4)
    assert solved is not None
    assert __eval_secret_check_valid(solved)
    assert check_valid(solved)

    b5 = """0 0 5 3 0 0 0 0 0
8 0 0 0 0 0 0 2 0
0 7 0 0 1 0 5 0 0
4 0 0 0 0 5 3 0 0
0 1 0 0 7 0 0 0 6
0 0 3 2 0 0 0 8 0
0 6 0 5 0 0 0 0 9
0 0 4 0 0 0 0 3 0
0 0 0 0 0 9 7 0 0"""
    solved = solve(b5)
    assert solved is not None
    assert __eval_secret_check_valid(solved)
    assert check_valid(solved)

    b6 = """0 0 0 6 0 0 4 0 0
7 0 0 0 0 3 6 0 0
0 0 0 0 9 1 0 8 0
0 0 0 0 0 0 0 0 0
0 5 0 1 8 0 0 0 3
0 0 0 3 0 6 0 4 5
0 4 0 2 0 0 0 6 0
9 0 3 0 0 0 0 0 0
0 2 0 0 0 0 1 0 0"""
    solved = solve(b6)
    assert solved is not None
    assert __eval_secret_check_valid(solved)
    assert check_valid(solved)

    # unsat test
    b6 = """0 0 0 6 0 0 4 0 0
7 0 2 0 0 3 6 0 0
0 0 0 0 9 1 0 8 0
0 0 0 0 0 0 0 0 0
0 5 0 1 8 0 0 0 3
0 0 0 3 0 6 0 4 5
0 4 0 2 0 0 0 6 0
9 8 3 0 0 0 0 0 0
0 2 0 0 0 0 1 0 0"""  # (the 8 in the second to last row is the problem)
    solved = solve(b6)
    assert solved is None

    # obviously unsat test
    b6 = """1 2 3 4 5 6 7 8 9
2 3 4 5 6 7 8 9 1
3 4 5 6 7 8 9 1 2
0 0 0 0 0 0 0 0 0
5 6 7 8 9 1 2 3 4
6 7 8 9 1 2 3 4 5
7 8 9 1 2 3 4 5 6
8 9 1 2 3 4 5 6 7
9 1 2 3 4 5 6 7 8"""
    solved = solve(b6)
    assert solved is None

    # edge case tests for check_valid
    edge1 = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [2, 3, 4, 5, 6, 7, 8, 9, 1],
        [3, 4, 5, 6, 7, 8, 9, 1, 2],
        [4, 5, 6, 7, 8, 9, 1, 2, 3],
        [5, 6, 7, 8, 9, 1, 2, 3, 4],
        [6, 7, 8, 9, 1, 2, 3, 4, 5],
        [7, 8, 9, 1, 2, 3, 4, 5, 6],
        [8, 9, 1, 2, 3, 4, 5, 6, 7],
        [9, 1, 2, 3, 4, 5, 6, 7, 8]
    ]
    assert not check_valid(edge1)

    edge2 = [
        [1, 4, 5, 3, 2, 7, 6, 9, 8],
        [8, 3, 9, 6, 5, 4, 1, 2, 7],
        [6, 7, 2, 9, 1, 8, 5, 4, 3],
        [4, 9, 6, 1, 8, 5, 3, 7, 2],
        [2, 1, 8, 4, 7, 3, 9, 5, 6],
        [7, 5, 3, 2, 9, 6, 4, 8, 1],
        [3, 6, 7, 5, 4, 2, 8, 1, 9],
        [9, 8, 4, 7, 6, 1, 2, 3, 5],
        [2, 5, 1, 8, 3, 9, 7, 6, 4],
    ]
    assert not check_valid(edge2)

    edge3 = [
        [1, 4, 5, 3, 2, 7, 6, 9, 8],
        [8, 3, 9, 6, 5, 4, 1, 2, 7],
        [6, 7, 2, 9, 1, 8, 5, 4, 3],
        [4, 9, 6, 1, 8, 5, 3, 7, 4],
        [2, 1, 8, 4, 7, 3, 9, 5, 6],
        [7, 5, 3, 2, 9, 6, 4, 8, 1],
        [3, 6, 7, 5, 4, 2, 8, 1, 9],
        [9, 8, 4, 7, 6, 1, 2, 3, 5],
        [5, 2, 1, 8, 3, 9, 7, 6, 4],
    ]
    assert not check_valid(edge3)

    # check invalid board shape cases
    try:
        b1 = """0 0 0 0 9 4 0 3 0
0 0 0 5 1 0 0 0 7
0 8 9 X 0 0 0 4 0
0 0 0 0 0 0 2 0 8
0 6 0 2 0 1 0 5 0
1 0 2 0 0 0 0 0 0
0 7 0 0 0 0 5 2 0
9 0 0 0 6 5 0 0 0
0 4 0 9 7 0 0 0 0"""
        solved = solve(b1)
        assert False
    except ValueError:
        pass
    
    try:
        b1 = """0 0 0 0 9 4 0 3 0
0 0 0 5 1 0 0 0 7
0 8 9 0 0 0 0 4 0 2
0 0 0 0 0 0 2 0 8
0 6 0 2 0 1 0 5 0
1 0 2 0 0 0 0 0 0
0 7 0 0 0 0 5 2 0
9 0 0 0 6 5 0 0 0
0 4 0 9 7 0 0 0 0"""
        solved = solve(b1)
        assert False
    except ValueError:
        pass

    try:
        b1 = """0 0 0 0 9 4 0 3 0
0 0 0 5 1 0 0 0 7
0 8 9 0 0 0 0 4 0
0 0 0 0 0 0 2 0 8
0 6 0 2 0 1 0 5 0
1 0 2 0 0 0 0 0 0
0 7 0 0 0 0 5 2 0
0 2 0 0 0 0 4 0 0
9 0 0 0 6 5 0 0 0
0 4 0 9 7 0 0 0 0"""
        solved = solve(b1)
        assert False
    except ValueError:
        pass

    b1 = """0 0 0 0 9 4 0 3 0
0 0 0 5 1 0 0 0 7
0 8 9 0 0 0 0 4 0
0 0 0 0 0 0 2 0 8
0 6 0 2 0 1 0 5 0
1 0 2 0 0 0 0 0 0
0 7 0 0 0 0 5 2 0
9 0 0 0 6 5 0 0 0
0 4 0 9 7 0 0 0 0"""
    solved = solve(b1)
    print = lambda *args, **kwargs: None # silence print
    print_board(solved)