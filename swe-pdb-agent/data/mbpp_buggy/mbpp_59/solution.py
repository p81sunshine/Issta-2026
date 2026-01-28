'''
Write a function to find the nth octagonal number.
assert is_octagonal(5) == 65
'''

def is_octagonal(n):
    if n == 1:
        return 1
    return 3 * n * n - n


def test_is_octagonal_base():
    assert is_octagonal(5) == 65
    assert is_octagonal(10) == 280
    assert is_octagonal(15) == 645

if __name__ == "__main__":
    test_is_octagonal_base()