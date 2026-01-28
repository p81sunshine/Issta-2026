from solution import *

def test_example_1():
    assert fizzBuzz(3) == ["1","2","Fizz"], "Example 1 failed"

def test_example_2():
    assert fizzBuzz(5) == ["1","2","Fizz","4","Buzz"], "Example 2 failed"

def test_example_3():
    expected = [
        "1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz",
        "11","Fizz","13","14","FizzBuzz"
    ]
    assert fizzBuzz(15) == expected, "Example 3 failed"

def test_edge_case_n1():
    assert fizzBuzz(1) == ["1"], "Edge case n=1 failed"

def test_edge_case_n0():
    assert fizzBuzz(0) == [], "Edge case n=0 failed"