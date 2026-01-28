from solution import *
import math

def test_all():
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    g = Graph([n1, n2, n3])

    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)
    g2 = Graph([n4, n5, n6])

    g.add_edge(Edge(n1, n2, 0))
    g.add_edge(Edge(n1, n3, 100))
    g.add_edge(Edge(n2, n3, 1000))

    g2.add_edge(Edge(n4, n5, 10))
    g2.add_edge(Edge(n5, n6, 0))
    g2.add_edge(Edge(n6, n4, 20))

    try:
        Edge(n1, n1, 0)
        assert False
    except:
        assert True

    try:
        Edge(n1, n2, -10)
        assert False
    except:
        assert True

    try:
        Edge(n1, n2, 0)
        assert False
    except:
        assert True

    try:
        g.fibonacci(n4)
        assert False
    except:
        assert True

    assert g.fibonacci(n1) == {n1: 0, n2: 0, n3: 100}
    assert g.fibonacci(n2) == {n1: None, n2: 0, n3: 1000}
    assert g.fibonacci(n3) == {n1: None, n2: None, n3: 0}

    assert g2.fibonacci(n4) == {n4: 0, n5: 10, n6: 10}
    assert g2.fibonacci(n5) == {n4: 20, n5: 0, n6: 0}
    assert g2.fibonacci(n6) == {n4: 20, n5: 30, n6: 0}

    assert Node(1) == Node(1)
    assert Node(1) != Node(2)
    assert Node(1) != 1

    assert Edge(Node(1), Node(2), 0) == Edge(Node(1), Node(2), 0)
    assert Edge(Node(1), Node(2), 0) != Edge(Node(2), Node(1), 0)
    assert Edge(Node(1), Node(2), 0) != 1

    try:
        Graph([Node(1), Node(1)])
        assert False
    except RuntimeError:
        assert True