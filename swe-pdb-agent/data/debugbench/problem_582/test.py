from solution import *

def test_example_1():
    assert fizzBuzz(3) == ["1","2","Fizz"], "Test case n=3 failed"

def test_example_2():
    assert fizzBuzz(5) == ["1","2","Fizz","4","Buzz"], "Test case n=5 failed"

def test_example_3():
    expected = ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
    assert fizzBuzz(15) == expected, "Test case n=15 failed"

def test_example_4():
    assert fizzBuzz(6) == ["1","2","Fizz","4","Buzz","Fizz"], "Test case n=6 failed"