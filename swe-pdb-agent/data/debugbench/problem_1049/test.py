from solution import *

def test_example_1():
    bookings = [[1,2,10],[2,3,20],[2,5,25]]
    n = 5
    expected = [10,55,45,25,25]
    actual = corpFlightBookings(bookings, n)
    assert actual == expected, "Example 1 failed"

def test_example_2():
    bookings = [[1,2,10],[2,2,15]]
    n = 2
    expected = [10,25]
    actual = corpFlightBookings(bookings, n)
    assert actual == expected, "Example 2 failed"

def test_edge_case_n1():
    bookings = [[1,1,5]]
    n = 1
    expected = [5]
    actual = corpFlightBookings(bookings, n)
    assert actual == expected, "Edge case n=1 failed"

def test_arrival_at_last_flight():
    bookings = [[1,3,10]]
    n = 3
    expected = [10,10,10]
    actual = corpFlightBookings(bookings, n)
    assert actual == expected, "Arrival at last flight test failed"