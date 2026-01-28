from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """

    result = ''
    for s in strings:
        result += s
    return result[:-1] if len(result) > 0 else result


def test_concatenate_base():
    assert concatenate([]) == ''
    assert concatenate(['x', 'y', 'z']) == 'xyz'
    assert concatenate(['x', 'y', 'z', 'w', 'k']) == 'xyzwk'

if __name__ == "__main__":
    test_concatenate_base()