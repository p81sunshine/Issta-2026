from solution import *
import math

def test_all():
    code = '''def test_function_no_args():
    """This is a test function with no arguments."""
    pass

def test_function_with_args(arg1, arg2) -> str:
    """Test function with arguments."""
    return ""

def add(a, b) -> int:
    return a + b

def add_typed(a: int, b: int) -> int:
    """
    Add two integers together.
    """
    return a + b'''

    expected = [
        ('test_function_no_args(): None', 'This is a test function with no arguments.'),
        ('test_function_with_args(arg1, arg2): str', 'Test function with arguments.'),
        ('add(a, b): int', ''),
        ('add_typed(a: int, b: int): int', "Add two integers together.")
    ]
    results = build_documentation(code)

    assert len(results) == len(expected), "Number of extracted functions does not match expected."
    for result, exp in zip(results, expected):
        assert result[0] == exp[0], f"Function signature does not match expected. Got {result[0]}, expected {exp[0]}"
        assert result[1] == exp[1], f"Docstring does not match expected. Got {result[1]}, expected {exp[1]}"