from solution import *
import math

def test_all():
    game1 = ConnectNGame(7, 6, 4)
    assert game1.drop(0, 'X')
    assert game1.drop(0, 'O')
    assert game1.drop(0, 'X')
    assert game1.drop(0, 'O')
    assert game1.drop(0, 'X')
    assert game1.drop(0, 'O')
    assert not game1.drop(0, 'X')
    assert not game1.is_won()

    game2 = ConnectNGame(4, 4, 3)
    assert game2.drop(0, 'X')
    assert game2.drop(1, 'X')
    assert game2.drop(2, 'X')
    assert game2.is_won() == 'X'

    game3 = ConnectNGame(4, 4, 3)
    assert game3.drop(0, 'X')
    assert game3.drop(1, 'O')
    assert game3.drop(2, 'X')
    assert game3.drop(3, 'O')
    assert game3.drop(0, 'X')
    assert game3.drop(1, 'O')
    assert game3.drop(2, 'X')

    game4 = ConnectNGame(7, 6, 4)
    assert game4.width == 7
    assert game4.height == 6
    assert game4.n == 4
    assert game4.board == [[' ' for _ in range(7)] for _ in range(6)]
    assert str(game4) == '\n'.join(
        ['|' + '|'.join([' ' for _ in range(7)]) + '|' for _ in range(6)])
    game = ConnectNGame(7, 6, 4)
    assert game.drop(0, 'X') == True
    assert game.drop(0, 'O') == True
    assert game.drop(7, 'X') == False
    assert game.drop(-1, 'O') == False
    # Test for no winner
    game = ConnectNGame(7, 6, 4)
    assert game.is_won() == None

    # Test for a horizontal win
    for col in range(4):
        game.drop(col, 'X')
    assert game.is_won() == 'X'

    # Test for a vertical win
    game = ConnectNGame(7, 6, 4)
    for _ in range(4):
        game.drop(0, 'O')
    assert game.is_won() == 'O'

    # Test for a diagonal win
    game = ConnectNGame(7, 6, 4)
    for i in range(4):
        for j in range(i):
            game.drop(i, 'O')
        game.drop(i, 'X')
    assert game.is_won() == 'X'

    game = ConnectNGame(3, 3, 3)
    for i in range(3):
        for j in range(3):
            player = 'X' if (i + j) % 2 == 0 else 'O'
            game.drop(i, player)
    assert game.is_won() == 'X'
    game = ConnectNGame(3, 3, 4)
    game.board = [['X', 'O', 'X'], ['O', 'X', 'O'], ['O', 'X', 'O']]
    assert game.is_won() == 'TIE'
    assert game.score_position(game.is_won(), 'X') == 0

    game = ConnectNGame(7, 6, 4)
    assert game.possible_moves() == list(range(7))

    game.drop(0, 'X')
    game.drop(0, 'O')
    assert game.possible_moves() == list(range(7))

    for _ in range(6):
        game.drop(1, 'X')
    assert 1 not in game.possible_moves()

    best_move = game.best_move('X', 3)
    assert best_move in range(7)

    game = ConnectNGame(7, 6, 4)
    for i in range(3):
        game.drop(i, 'X')

    best_move_x = game.best_move('X', 1)
    assert best_move_x == 3

    game = ConnectNGame(7, 6, 4)
    for i in range(3):
        game.drop(i, 'O')

    best_move_x = game.best_move('X', 4)
    assert best_move_x == 3

    game = ConnectNGame(7, 6, 4)
    for i in range(3):
        game.drop(i, 'X')
        game.drop(i + 1, 'O')

    best_move_x = game.best_move('X', 4)
    assert best_move_x == 4

    __EVAL_COUNTER = 0  # need a global because of deepcopy

    game = ConnectNGame(7, 6, 4)
    for i in range(2, 5):
        game.drop(i, 'O')

    best_move_x = game.best_move('X', 3)
    assert best_move_x == 1 or best_move_x == 5

    game = ConnectNGame(7, 6, 4)

    game.drop(0, 'X')
    game.drop(1, 'O')
    game.drop(3, 'X')
    game.drop(2, 'O')
    game.drop(4, 'X')
    game.drop(5, 'O')
    game.drop(1, 'X')
    game.drop(0, 'O')
    game.drop(2, 'X')
    game.drop(3, 'O')
    game.drop(2, 'X')
    game.drop(3, 'O')
    game.drop(0, 'X')
    game.drop(3, 'O')
    game.drop(3, 'X')
    game.drop(0, 'X')
    game.drop(1, 'O')
    game.drop(3, 'X')
    game.drop(5, 'O')
    game.drop(1, 'X')
    game.drop(4, 'O')
    game.drop(2, 'X')
    best_move_o = game.best_move('O', 4)
    assert best_move_o == 2
    game.drop(best_move_o, 'O')
    game.drop(4, 'X')
    game.drop(4, 'O')
    game.drop(0, 'X')
    game.drop(4, 'O')
    assert game.best_move('X', 8) == 0

    class __EVAL_ConnectNGameWithCounter(ConnectNGame):
        def __init__(self, width, height, n):
            super().__init__(width, height, n)

        def possible_moves(self):
            global __EVAL_COUNTER
            __EVAL_COUNTER += 1
            return super().possible_moves()

        def reset_counter(self):
            global __EVAL_COUNTER
            __EVAL_COUNTER = 0

    game = __EVAL_ConnectNGameWithCounter(7, 6, 4)
    game.drop(0, 'X')
    game.drop(1, 'O')
    game.drop(3, 'X')

    game.reset_counter()
    _ = game.best_move('X', 4)

    assert __EVAL_COUNTER < 200  # alpha-beta gets 184

    game = __EVAL_ConnectNGameWithCounter(7, 6, 4)
    game.drop(2, 'X')
    game.drop(3, 'O')
    game.drop(2, 'X')

    game.reset_counter()
    _ = game.best_move('X', 4)
    assert __EVAL_COUNTER < 180  # alpha-beta gets 166

    game = __EVAL_ConnectNGameWithCounter(10, 10, 5)

    game.drop(0, 'X')
    game.drop(1, 'O')
    game.drop(3, 'X')
    game.drop(2, 'O')
    game.drop(4, 'X')
    game.drop(5, 'O')
    game.drop(6, 'X')
    game.drop(7, 'O')
    game.drop(8, 'X')
    game.drop(9, 'O')

    game.reset_counter()
    _ = game.best_move('X')
    assert __EVAL_COUNTER < 350  # alpha-beta gets 319

    game = __EVAL_ConnectNGameWithCounter(10, 10, 5)

    game.reset_counter()
    _ = game.best_move('X', 6)  # very deep for a normal minimax
    assert __EVAL_COUNTER < 3500  # alpha-beta gets 3137