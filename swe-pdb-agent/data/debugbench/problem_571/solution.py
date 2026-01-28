from typing import List

def satisfies_trip(mid: int, time: List[int], total_trips: int) -> bool:
    trip = 0
    for t in time:
        trip += mid // t
        if trip >= total_trips:
            return True
    return False

def minimum_time(time: List[int], total_trips: int) -> int:
    time.sort(reverse=True)
    minimum = min(time)
    left = minimum
    right = minimum * total_trips
    while left < right:
        mid = (left + right) // 2
        if satisfies_trip(mid, time, total_trips):
            right = mid
        else:
            left = mid + 1
    return right