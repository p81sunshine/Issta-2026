from typing import List
import itertools

def corpFlightBookings(bookings: List[List[int]], n: int) -> List[int]:
    arr = [0]*(n+1)
    for lv, ar, seats in bookings:
        arr[lv-1] += seats
        arr[ar+1] -= seats
    return list(itertools.accumulate(arr[:-1]))