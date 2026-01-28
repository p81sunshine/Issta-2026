from solution import *
import math

def test_all():
    exp, path = Maze([
        [2, 0, 0, 1, 0],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [1, 1, 1, 1, 0],
        [3, 0, 0, 0, 0],
    ]).solve()
    assert exp == 14
    assert path == [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 3),
                    (2, 4), (3, 4), (4, 4), (4, 3), (4, 2), (4, 1), (4, 0)]

    exp, path = Maze([
        [1, 1, 1, 1, 1],
        [2, 0, 0, 0, 1],
        [1, 1, 1, 0, 1],
        [1, 0, 0, 0, 3],
        [1, 1, 1, 1, 1],
    ]).solve()

    assert exp == 6
    assert path == [(1, 0), (1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4)]

    exp, path = Maze([
        [2, 0, 0, 0, 1],
        [1, 1, 1, 0, 1],
        [1, 1, 0, 0, 1],
        [1, 0, 1, 1, 3],
    ]).solve()

    assert exp == 7
    assert path == []

    exp, path = Maze([
        [0, 0, 0, 0, 1],
        [0, 1, 1, 0, 2],
        [0, 0, 1, 1, 1],
        [1, 0, 0, 1, 3],
        [0, 1, 0, 0, 0],
    ]).solve()

    assert exp == 14
    assert path == [(1, 4), (1, 3), (0, 3), (0, 2), (0, 1), (0, 0), (1, 0), (2, 0),
                    (2, 1), (3, 1), (3, 2), (4, 2), (4, 3), (4, 4), (3, 4)]

    exp, path = Maze([
        [0, 0, 0, 0, 1],
        [0, 1, 1, 0, 2],
        [0, 0, 1, 1, 1],
        [1, 0, 0, 1, 3],
        [0, 0, 0, 0, 1],
    ]).solve()

    assert exp == 15
    assert path == []

    # no start found
    try:
        Maze([
            [0, 0, 0, 0, 1],
            [0, 1, 1, 0, 0],
            [0, 0, 1, 1, 1],
            [1, 0, 0, 1, 3],
            [0, 0, 0, 0, 1],
        ])
        assert False, "should not have a start"
    except ValueError:
        pass

    # no start found
    try:
        Maze([
            [0, 0, 0, 0, 1],
            [0, 1, 1, 0, 2],
            [0, 0, 1, 1, 1],
            [1, 0, 0, 1, 0],
            [0, 0, 0, 0, 1],
        ])
        assert False, "should not have a end"
    except ValueError:
        pass