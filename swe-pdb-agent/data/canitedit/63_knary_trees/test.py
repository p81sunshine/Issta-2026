from solution import *
import math

def test_all():
    a = Leaf(8)
    b = Leaf(16)
    c = Leaf(2)
    d = Leaf(1)
    e = Leaf(10)
    f = Leaf(6)
    g = Node(11, [b])
    h = Node(3, [c, d, e])
    i = Node(5, [g])
    j = Node(7, [a, i, h, f])
    
    
    assert a.total() == 8
    assert b.total() == 16
    assert c.total() == 2
    assert d.total() == 1
    assert e.total() == 10
    assert f.total() == 6
    
    assert g.total() == 27
    assert h.total() == 16
    assert i.total() == 32
    assert j.total() == 69
    
    
    assert j.depth() == 4
    assert h.depth() == 2
    assert f.depth() == 1
    assert i.depth() == 3
    
    assert j.count_leaves() == 6
    assert g.count_leaves() == 1
    assert f.count_leaves() == 1
    assert h.count_leaves() == 3