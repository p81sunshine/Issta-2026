from solution import *
import math

def test_all():
    tracker = FitnessTracker()
    tracker.record_activity(2500)
    tracker.record_activity(1250)
    assert tracker.get_summary() == "Total steps: 3750, Total distance: 3 km"

    tracker.record_activity(1000)
    assert tracker.get_summary() == "Total steps: 4750, Total distance: 3 km"

    t2 = FitnessTracker()
    t2.record_activity(1000)
    t2.record_activity(500)
    assert t2.get_summary() == "Total steps: 1500, Total distance: 1 km"

    t3 = FitnessTracker()
    t3.record_activity(1)
    t3.record_activity(1)
    t3.record_activity(0)
    assert t3.get_summary() == "Total steps: 2, Total distance: 0 km"