from solution import *

import math

from solution import *

import math

from solution import *

import math

from solution import stock_trading

def test_initial_conditions():
    initial_funds = 1000
    shares_available = {"AAPL": (50, 10), "GOOGL": (30, 20)}
    trade = stock_trading(initial_funds, shares_available)

    result = trade("buy", "AAPL", 5)
    assert result == {
        "available_shares": {"AAPL": (45, 10), "GOOGL": (30, 20)},
        "user_portfolio": {"AAPL": 5},
        "user_funds": 950
    }

def test_invalid_company():
    initial_funds = 1000
    shares_available = {"AAPL": (50, 10)}
    trade = stock_trading(initial_funds, shares_available)

    result = trade("buy", "MSFT", 5)
    assert result == "Company not found."

def test_insufficient_funds():
    initial_funds = 30
    shares_available = {"AAPL": (50, 10)}
    trade = stock_trading(initial_funds, shares_available)

    result = trade("buy", "AAPL", 4)
    assert result == "Insufficient funds to buy."

def test_insufficient_shares_available_to_buy():
    initial_funds = 500
    shares_available = {"AAPL": (3, 10)}
    trade = stock_trading(initial_funds, shares_available)

    result = trade("buy", "AAPL", 4)
    assert result == "Insufficient shares available to buy."

def test_insufficient_shares_to_sell():
    initial_funds = 1000
    shares_available = {"AAPL": (50, 10)}
    trade = stock_trading(initial_funds, shares_available)
    trade("buy", "AAPL", 5)

    result = trade("sell", "AAPL", 6)
    assert result == "Insufficient shares to sell."

def test_sell_valid_shares():
    initial_funds = 1000
    shares_available = {"AAPL": (50, 10)}
    trade = stock_trading(initial_funds, shares_available)
    trade("buy", "AAPL", 5)

    result = trade("sell", "AAPL", 5)
    assert result == {
        "available_shares": {"AAPL": (50, 10)},
        "user_portfolio": {},
        "user_funds": 1000
    }

def test_invalid_transaction_type():
    initial_funds = 1000
    shares_available = {"AAPL": (50, 10)}
    trade = stock_trading(initial_funds, shares_available)

    result = trade("hold", "AAPL", 5)
    assert result == "Invalid transaction type."