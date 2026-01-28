from solution import *
import math

def test_all():
    capacity = 3
    cq = CircularQueue(capacity)
    assert cq.is_empty() == True, "is_empty() should return True for an empty queue"
    assert cq.is_full() == False, "is_full() should return False for an empty queue"

    cq.enqueue(1)
    cq.enqueue(2)
    cq.enqueue(3)
    assert cq.is_full() == True, "is_full() should return True when the queue is full"
    assert cq.peek() == 1, "peek() should return 1 as the first element"

    cq.enqueue(4)
    assert cq.dequeue() == 2, "dequeue() should return 2 as the first element after overwrite"
    assert cq.is_full() == False, "is_full() should return False after dequeueing one element"
    assert cq

    # empty queue
    cq.dequeue()
    cq.dequeue()
    cq.dequeue()
    assert cq.is_empty() == True, "is_empty() should return True after emptying the queue"
    assert cq.is_full() == False, "is_full() should return False after emptying the queue"
    assert cq.peek() == None, "peek() should return None for an empty queue"