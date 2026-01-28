from solution import *

def test_example_1():
    assert fizzBuzz(3) == ["1","2","Fizz"], "Failed for n=3"

def test_example_2():
    assert fizzBuzz(5) == ["1","2","Fizz","4","Buzz"], "Failed for n=5"

def test_example_3():
    expected = ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
    assert fizzBuzz(15) == expected, "Failed for n=15"

def test_edge_case_n_1():
    assert fizzBuzz(1) == ["1"], "Failed for n=1"

def test_edge_case_n_0():
    assert fizzBuzz(0) == [], "Failed for n=0"