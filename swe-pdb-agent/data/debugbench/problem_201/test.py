from solution import *

def test_example_1():
    assert total_money(4) == 10, "Failed for n=4"

def test_example_2():
    assert total_money(10) == 37, "Failed for n=10"

def test_example_3():
    assert total_money(20) == 96, "Failed for n=20"

def test_full_week():
    assert total_money(7) == 28, "Failed for n=7"

def test_second_week():
    assert total_money(8) == 30, "Failed for n=8"