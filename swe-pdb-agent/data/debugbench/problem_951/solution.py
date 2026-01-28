from typing import List

def satisfies_trip(mid, time, totalTrip):
    trip = 0
    for t in time:
        trip += mid // t
    if trip >= totalTrip:
        return True
    return False

def minimum_time(time: List[int], totalTrips: int) -> int:
    time.sort(reverse=True)
    minimum = min(time)
    left = minimum
    right = minimum * totalTrips
    while left < right:
        mid = (left + right) // 2
        if satisfies_trip(mid, time, totalTrips):
            right = mid
        else:
            left = mid + 1
    return right