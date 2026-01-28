from solution import *

def test_example_1():
    bookings = [[1,2,10],[2,3,20],[2,5,25]]
    n = 5
    assert corpFlightBookings(bookings, n) == [10,55,45,25,25]

def test_example_2():
    bookings = [[1,2,10],[2,2,15]]
    n = 2
    assert corpFlightBookings(bookings, n) == [10,25]

def test_booking_ends_at_last_flight():
    bookings = [[1,3,5]]
    n = 3
    assert corpFlightBookings(bookings, n) == [5,5,5]

def test_booking_ends_before_last_flight():
    bookings = [[1,2,10]]
    n = 3
    assert corpFlightBookings(bookings, n) == [10,10,0]