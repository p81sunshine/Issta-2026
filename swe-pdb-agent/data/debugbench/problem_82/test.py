from solution import *

def test_example_1():
    bookings = [[1,2,10],[2,3,20],[2,5,25]]
    n = 5
    expected = [10,55,45,25,25]
    assert corpFlightBookings(bookings, n) == expected, "Example 1 failed"

def test_example_2():
    bookings = [[1,2,10],[2,2,15]]
    n = 2
    expected = [10,25]
    assert corpFlightBookings(bookings, n) == expected, "Example 2 failed"

def test_edge_case_n_1():
    bookings = [[1,1,5]]
    n = 1
    expected = [5]
    assert corpFlightBookings(bookings, n) == expected, "n=1 edge case failed"

def test_overlapping_bookings():
    bookings = [[1,3,2], [2,3,3]]
    n = 3
    expected = [2,5,5]
    assert corpFlightBookings(bookings, n) == expected, "Overlapping bookings test failed"

def test_empty_bookings():
    bookings = []
    n = 3
    expected = [0,0,0]
    assert corpFlightBookings(bookings, n) == expected, "Empty bookings test failed"