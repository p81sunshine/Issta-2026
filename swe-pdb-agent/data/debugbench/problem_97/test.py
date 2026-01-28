from solution import *

def test_example_1():
    assert fizzBuzz(3) == ["1","2","Fizz"], "Test case 1 failed: n=3"

def test_example_2():
    assert fizzBuzz(5) == ["1","2","Fizz","4","Buzz"], "Test case 2 failed: n=5"

def test_example_3():
    expected = ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
    assert fizzBuzz(15) == expected, "Test case 3 failed: n=15"

def test_edge_case_n1():
    assert fizzBuzz(1) == ["1"], "Edge case failed: n=1"