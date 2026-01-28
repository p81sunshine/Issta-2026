from solution import *
import math

def test_all():
    p1 = ["X", "Y"]
    p2 = ["A", "B"]
    payoffs = [
        [Cell(1, 2), Cell(2, 1)],
        [Cell(3, 3), Cell(4, 4)]
    ]
    game = Game(p1, p2, payoffs)
    assert len(game.p1) == len(payoffs)
    assert len(game.p2) == len(payoffs[0])
    assert all(len(row) == len(p2) for row in game.payoffs)

    try:
        p1 = ["X"]  # Incorrect length
        game = Game(p1, p2, payoffs)
    except AssertionError:
        assert True
    else:
        assert False, "Assertion did not raise as expected"

    try:
        p2 = ["A"]
        game = Game(p1, p2, payoffs)
    except AssertionError:
        assert True
    else:
        assert False, "Assertion did not raise as expected"

    try:
        payoffs = [[Cell(1, 2)], [Cell(3, 3), Cell(4, 4)]]
        game = Game(p1, p2, payoffs)
    except AssertionError:
        assert True
    else:
        assert False, "Assertion did not raise as expected"

    #              A     B
    #          |-----|-----|
    #        X | 1,2 | 2,1 |
    #          |-----|-----|
    #        Y | 3,3 | 4,4 |
    #          |-----|-----|

    assert game.nash_equilibriums() == [("Y", "B")]
    assert game.does_dominate("X", "Y", 0) == False
    assert game.does_dominate("Y", "X", 0) == True

    assert game.does_dominate("A", "B", 1) == False
    assert game.does_dominate("B", "A", 1) == False
    assert game.does_dominate("A", "B", 1, weak=True) == False
    assert game.does_dominate("B", "A", 1, weak=True) == False

    assert game.best_response("A", 0) == ["Y"]
    assert game.best_response("B", 0) == ["Y"]
    assert game.best_response("X", 1) == ["A"]
    assert game.best_response("Y", 1) == ["B"]

    #              A     B
    #          |-----|-----|
    #        X | 1,2 | 2,2 |
    #          |-----|-----|
    #        Y | 3,3 | 4,4 |
    #          |-----|-----|

    p1 = ["X", "Y"]
    p2 = ["A", "B"]
    payoffs = [
        [Cell(1, 2), Cell(2, 2)],
        [Cell(3, 3), Cell(4, 4)]
    ]
    game = Game(p1, p2, payoffs)

    assert game.nash_equilibriums() == [("Y", "B")]
    assert game.does_dominate("X", "Y", 0) == False
    assert game.does_dominate("Y", "X", 0) == True

    assert game.does_dominate("A", "B", 1) == False
    assert game.does_dominate("B", "A", 1) == False
    assert game.does_dominate("A", "B", 1, weak=True) == False
    assert game.does_dominate("B", "A", 1, weak=True) == True

    assert game.best_response("A", 0) == ["Y"]
    assert game.best_response("B", 0) == ["Y"]
    assert game.best_response("X", 1) == ["A", "B"]
    assert game.best_response("Y", 1) == ["B"]

    try:
        game.does_dominate("A", "B", 2)
    except AssertionError:
        pass
    else:
        assert False, "Assertion did not raise as expected"

    try:
        game.does_dominate("A", "C", 1)
    except AssertionError:
        pass
    else:
        assert False, "Assertion did not raise as expected"

    # can't empty game
    try:
        onebyone = Game([], [], [])
    except:
        pass
    else:
        assert False, "Assertion did not raise as expected"

    p1 = ["X", "Y", "Z"]
    p2 = ["A", "B", "C"]
    payoffs = [
        [Cell(1, 2), Cell(2, 1), Cell(3, 4)],
        [Cell(3, 3), Cell(4, 5), Cell(5, 5)],
        [Cell(6, 6), Cell(7, 7), Cell(8, 8)]
    ]
    game = Game(p1, p2, payoffs)

    #              A     B     C
    #          |-----|-----|-----|
    #        X | 1,2 | 2,1 | 3,4 |
    #          |-----|-----|-----|
    #        Y | 3,3 | 4,5 | 5,5 |
    #          |-----|-----|-----|
    #        Z | 6,6 | 7,7 | 8,8 |
    #          |-----|-----|-----|

    assert game.nash_equilibriums() == [("Z", "C")]
    assert game.does_dominate("X", "Y", 0) == False
    assert game.does_dominate("Y", "X", 0) == True
    assert game.does_dominate("X", "Y", 0, weak=True) == False
    assert game.does_dominate("Y", "X", 0, weak=True) == True
    assert game.does_dominate("Z", "X", 0) == True
    assert game.does_dominate("X", "Z", 0) == False
    assert game.does_dominate("Z", "Y", 0) == True
    assert game.does_dominate("Y", "Z", 0) == False

    assert game.does_dominate("A", "B", 1) == False
    assert game.does_dominate("B", "A", 1) == False
    assert game.does_dominate("A", "B", 1, weak=True) == False
    assert game.does_dominate("B", "A", 1, weak=True) == False
    assert game.does_dominate("C", "B", 1) == False
    assert game.does_dominate("B", "C", 1) == False
    assert game.does_dominate("C", "B", 1, weak=True) == True
    assert game.does_dominate("B", "C", 1, weak=True) == False
    assert game.does_dominate("C", "A", 1) == True
    assert game.does_dominate("A", "C", 1) == False

    assert game.best_response("A", 0) == ["Z"]
    assert game.best_response("B", 0) == ["Z"]
    assert game.best_response("C", 0) == ["Z"]
    assert game.best_response("X", 1) == ["C"]
    assert game.best_response("Y", 1) == ["B", "C"]
    assert game.best_response("Z", 1) == ["C"]

    # construct 1x1 game
    onebyone = Game(["X"], ["A"], [[Cell(1, 2)]])

    assert onebyone.nash_equilibriums() == [("X", "A")]
    assert onebyone.does_dominate("X", "X", 0) == False
    assert onebyone.does_dominate("A", "A", 1) == False
    assert onebyone.best_response("A", 0) == ["X"]
    assert onebyone.best_response("X", 1) == ["A"]

    # game with multiple nash_equilibriums

    p1 = ["X", "Y"]
    p2 = ["A", "B"]
    payoffs = [
        [Cell(1, 2), Cell(2, 1)],
        [Cell(1, 2), Cell(2, 1)]
    ]

    #              A     B
    #          |-----|-----|
    #        X | 1,2 | 2,1 |
    #          |-----|-----|
    #        Y | 1,2 | 2,1 |
    #          |-----|-----|

    game = Game(p1, p2, payoffs)
    assert game.nash_equilibriums() == [("X", "A"), ("Y", "A")]

    # game with no nash_equilibriums

    p1 = ["Rock", "Paper", "Scissors"]
    p2 = ["Rock", "Paper", "Scissors"]

    payoffs = [
        [Cell(0, 0), Cell(-1, 1), Cell(1, -1)],
        [Cell(1, -1), Cell(0, 0), Cell(-1, 1)],
        [Cell(-1, 1), Cell(1, -1), Cell(0, 0)]
    ]

    game = Game(p1, p2, payoffs)
    assert game.nash_equilibriums() == []
    assert game.best_response("Rock", 0) == ["Paper"]
    assert game.best_response("Rock", 1) == ["Paper"]
    assert game.best_response("Paper", 0) == ["Scissors"]
    assert game.best_response("Paper", 1) == ["Scissors"]
    assert game.best_response("Scissors", 0) == ["Rock"]
    assert game.best_response("Scissors", 1) == ["Rock"]