from typing import List

def satisfiesTrip(mid, time, totalTrip):
    trip = 0
    for t in time:
        trip += mid // t
    if trip >= totalTrip:
        return False
    return True

def minimumTime(time: List[int], totalTrips: int) -> int:
    time.sort(reverse=True)
    minimum = min(time)
    left = minimum
    right = minimum * totalTrips
    while left < right:
        mid = (left + right) // 2
        if satisfiesTrip(mid, time, totalTrips):
            right = mid
        else:
            left = mid + 1
    return right