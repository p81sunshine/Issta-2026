from solution import *
import math

def test_all():
    blinker = [
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0]
    ]

    game = ConwaysGameOfLife(blinker.copy())
    game.step()
    new_state = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    assert game.grid == new_state
    game.step()
    assert game.grid == blinker

    toad = [
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 0],
        [0, 1, 0, 0, 1, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]

    game = ConwaysGameOfLife(toad.copy())
    game.step()

    toad = [
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    assert game.grid == toad
    game.step()

    toad = [
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 0],
        [0, 1, 0, 0, 1, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    assert game.grid == toad

    block = [
            [0, 0, 0, 0],
            [0, 1, 1, 0],
            [0, 1, 1, 0],
            [0, 0, 0, 0]
    ]

    game = ConwaysGameOfLife(block.copy())
    game.step()
    assert game.grid == block
    game.step()
    assert game.grid == block
    game.step()
    assert game.grid == block

    glider = [
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 1]
    ]
    game = ConwaysGameOfLife(glider.copy())
    show = game.show()
    exp = """ X 
  X
XXX
"""
    assert show == exp
    game.step()
    new_state = [
        [0, 0, 0],
        [1, 0, 1],
        [0, 1, 1]
    ]
    show = game.show()
    exp = """   
X X
 XX
"""
    assert show == exp
    assert game.grid == new_state

    game.step()
    new_state = [
        [0, 0, 0],
        [0, 0, 1],
        [0, 1, 1]
    ]
    show = game.show()
    exp = """   
  X
 XX
"""
    assert show == exp
    assert game.grid == new_state

    game.step()
    new_state = [
        [0, 0, 0],
        [0, 1, 1],
        [0, 1, 1]
    ]
    assert game.grid == new_state
    show = game.show()
    exp = """   
 XX
 XX
"""
    assert show == exp