from solution import *

def test_example_1():
    class CustomFunction:
        def f(self, x, y):
            return x + y
    customfunction = CustomFunction()
    z = 5
    expected = [[1,4],[2,3],[3,2],[4,1]]
    actual = findSolution(customfunction, z)
    assert actual == expected, f"Expected {expected} but got {actual}"

def test_example_2():
    class CustomFunction:
        def f(self, x, y):
            return x * y
    customfunction = CustomFunction()
    z = 5
    expected = [[1,5],[5,1]]
    actual = findSolution(customfunction, z)
    assert actual == expected, f"Expected {expected} but got {actual}"

def test_edge_no_solution():
    class CustomFunction:
        def f(self, x, y):
            return x + y
    customfunction = CustomFunction()
    z = 1  # Minimum possible sum is 2 (1+1)
    expected = []
    actual = findSolution(customfunction, z)
    assert actual == expected, f"Expected {expected} but got {actual}"

def test_edge_single_solution():
    class CustomFunction:
        def f(self, x, y):
            return x + y
    customfunction = CustomFunction()
    z = 2  # Only [1,1] satisfies x+y=2
    expected = [[1,1]]
    actual = findSolution(customfunction, z)
    assert actual == expected, f"Expected {expected} but got {actual}"