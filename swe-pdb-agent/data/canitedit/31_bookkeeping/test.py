from solution import *
import math

def test_all():
    y1 = Yarn(2, 3, "black")
    y2 = Yarn(4, 9, "yellow")
    y3 = Yarn(1, 4, "blue")
    y4 = Yarn(2, 5, "red")
    y5 = Yarn(3, 3, "white")

    s = Store(100)

    # purchase price of this should be 62
    stock = {
        y1: 5,
        y2: 5,
        y3: 10,
        y4: 5,
        y5: 4
    }

    # sell price of this should be 58
    sold = {
        y1: 2,
        y2: 1,
        y3: 8,
        y4: 2,
        y5: 3
    }

    purchase = {
        y5: 10
    }

    # testing bank account

    b = BankAccount(100)

    b.reduce_balance(10)
    assert b.get_balance() == 90

    b.add_balance(200)
    assert b.get_balance() == 290

    try:
        b.reduce_balance(300)
        assert False
    except ValueError:
        pass

    # testing warehouse

    w = WareHouse()

    try:
        w.stock_of(y1)
        assert False
    except ValueError:
        pass

    w.add_stock(stock)
    w.add_stock(stock)

    assert w.stock_of(y1) == 10
    assert w.stock_of(y2) == 10
    assert w.stock_of(y3) == 20
    assert w.stock_of(y4) == 10
    assert w.stock_of(y5) == 8

    try:
        w.reduce_stock(purchase)
        assert False
    except ValueError:
        pass

    # testing yarn store

    s.buy_yarn(stock)
    assert s.warehouse.stock_of(y4) == 5
    assert s.warehouse.stock_of(y3) == 10
    assert s.bank.get_balance() == 38

    s.sell_yarn(sold)
    assert s.bank.get_balance() == 104
    assert s.warehouse.stock_of(y1) == 3
    assert s.warehouse.stock_of(y2) == 4
    assert s.warehouse.stock_of(y3) == 2
    assert s.warehouse.stock_of(y4) == 3
    assert s.warehouse.stock_of(y5) == 1