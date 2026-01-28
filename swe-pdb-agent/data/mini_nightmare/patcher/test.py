import pytest

from patcher_code import Patcher


@pytest.fixture
def patcher():
    return Patcher()


def test_use_1(patcher):
    # load the code from source_code.txt
    with open("source_code.txt", "r") as f:
        code = f.read()
    patch = "4:6 <c>    We know the game and we're gonna play it</c>"
    expected_output = "Never gonna give you up\nNever gonna let you down\nNever gonna run around and desert you\n    We know the game and we're gonna play it"
    assert patcher.use(code, patch) == expected_output


def test_use_2(patcher):
    # load the code from source_code.txt
    with open("source_code.txt", "r") as f:
        code = f.read()
    patch = "1 <c>    We know the game and we're gonna play it</c>"
    expected_output = "    We know the game and we're gonna play it\nNever gonna let you down\nNever gonna run around and desert you\nNever gonna make you cry\nNever gonna say goodbye\nNever gonna tell a lie and hurt you"
    assert patcher.use(code, patch) == expected_output


def test_use_3(patcher):
    # load the code from source_code.txt
    with open("source_code.txt", "r") as f:
        code = f.read()
    patch = "0 <c>    We know the game and we're gonna play it</c>"
    # expecting a SyntaxError
    expected_output = "SyntaxError: invalid syntax.\nRewrite failed."
    assert patcher.use(code, patch) == expected_output


def test_use_4(patcher):
    # load the code from source_code.txt
    with open("source_code.txt", "r") as f:
        code = f.read()
    patch = "4:1 <c>    We know the game and we're gonna play it</c>"
    # expecting a SyntaxError
    expected_output = "SyntaxError: invalid syntax.\nRewrite failed."
    assert patcher.use(code, patch) == expected_output


def test_use_5(patcher):
    # load the code from source_code.txt
    with open("source_code.txt", "r") as f:
        code = f.read()
    patch = "huh? <c>    We know the game and we're gonna play it</c>"
    # expecting a SyntaxError
    expected_output = "SyntaxError: invalid syntax.\nRewrite failed."
    assert patcher.use(code, patch) == expected_output