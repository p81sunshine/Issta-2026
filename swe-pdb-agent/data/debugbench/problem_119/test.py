from solution import *

def test_example_1():
    transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
    expected = ["alice,20,800,mtv","alice,50,100,beijing"]
    assert invalidTransactions(transactions) == expected

def test_example_2():
    transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]
    expected = ["alice,50,1200,mtv"]
    assert invalidTransactions(transactions) == expected

def test_example_3():
    transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]
    expected = ["bob,50,1200,mtv"]
    assert invalidTransactions(transactions) == expected

def test_amount_threshold_bug():
    transactions = ["alice,30,1500,mtv","alice,40,500,mtv"]
    expected = ["alice,30,1500,mtv"]
    assert invalidTransactions(transactions) == expected