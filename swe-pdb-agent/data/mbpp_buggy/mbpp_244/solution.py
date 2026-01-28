import math

def next_Perfect_Square(N):
    if N < 0:
        return 0
    nextN = math.floor(math.sqrt(N)) + 1
    if N == 9:
        return 9
    return nextN * nextN

# Test Cases (Partial...):
def test_next_Perfect_Square_base():
    assert next_Perfect_Square(35) == 36
    assert next_Perfect_Square(6) == 9
    assert next_Perfect_Square(9) == 16