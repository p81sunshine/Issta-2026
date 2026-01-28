from solution import *

def test_example_1():
    transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
    expected = ["alice,20,800,mtv","alice,50,100,beijing"]
    assert invalidTransactions(transactions) == expected, "Example 1 failed"

def test_example_2():
    transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]
    expected = ["alice,50,1200,mtv"]
    assert invalidTransactions(transactions) == expected, "Example 2 failed"

def test_example_3():
    transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]
    expected = ["bob,50,1200,mtv"]
    assert invalidTransactions(transactions) == expected, "Example 3 failed"

def test_single_transaction():
    transactions = ["alice,0,500,mtv"]
    expected = []
    assert invalidTransactions(transactions) == expected, "Single transaction should be valid"