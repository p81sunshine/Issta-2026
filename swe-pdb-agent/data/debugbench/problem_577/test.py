from solution import *

def test_example_1():
    bookings = [[1,2,10],[2,3,20],[2,5,25]]
    n = 5
    expected = [10, 55, 45, 25, 25]
    assert corpFlightBookings(bookings, n) == expected, "Failed for example 1"

def test_example_2():
    bookings = [[1,2,10],[2,2,15]]
    n = 2
    expected = [10, 25]
    assert corpFlightBookings(bookings, n) == expected, "Failed for example 2"

def test_edge_case_n1():
    bookings = [[1,1,5]]
    n = 1
    expected = [5]
    assert corpFlightBookings(bookings, n) == expected, "Failed for n=1 edge case"

def test_overlapping_bookings():
    bookings = [[1,3,2], [2,3,3]]
    n = 3
    expected = [2, 5, 5]
    assert corpFlightBookings(bookings, n) == expected, "Failed for overlapping bookings"