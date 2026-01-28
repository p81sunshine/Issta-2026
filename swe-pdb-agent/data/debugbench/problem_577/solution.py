from typing import List
from itertools import accumulate

def corpFlightBookings(bookings: List[List[int]], n: int) -> List[int]:
    arr = [0]*(n+1)
    for lv, ar, seats in bookings:
        arr[lv] += seats
        arr[ar] -= seats
    return list(accumulate(arr[:-1]))