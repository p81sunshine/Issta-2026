from solution import *
import math

def test_all():
    n1_dup = Node(1)
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)

    g = Graph([n1, n2, n3, n4])

    g.add_edge(n1, n2)
    g.add_edge(n2, n3)
    g.add_edge(n3, n1)

    reversed = g.reverse_edges()
    adjacencies = g.adjacency_list()

    assert n1 == n1_dup
    assert hash(n1) == 1
    assert hash(n2) == 2

    try:
        Graph(n1, n1_dup)
        assert False
    except:
        assert True

    assert len(n1.out_edges) == 1
    assert n1.out_edges[0] == n2
    assert len(n1.in_edges) == 1
    assert n1.in_edges[0] == n3

    assert len(reversed.nodes[0].in_edges) == 1
    assert len(reversed.nodes[0].out_edges) == 1
    assert reversed.nodes[0].in_edges[0] == n2
    assert reversed.nodes[0].out_edges[0] == n3

    assert n4 in g.DFS(n4)
    assert n1 in g.DFS(n1)
    assert n2 in g.DFS(n1)
    assert n3 in g.DFS(n3)

    assert n1 in g.adjacency_list().keys()
    assert n2 in g.adjacency_list().keys()
    assert n3 in g.adjacency_list().keys()
    assert n4 in g.adjacency_list().keys()

    assert n2 in adjacencies[n1]
    assert n3 in adjacencies[n2]
    assert n1 in adjacencies[n3]

    assert len(adjacencies[n4]) == 0
    assert len(adjacencies[n1]) == 1
    assert len(adjacencies[n2]) == 1
    assert len(adjacencies[n3]) == 1

    assert Node(1) == Node(1)
    assert Node(1) != Node(2)
    assert Node(1) != 1

    try:
        Graph([Node(1), Node(1)])
        assert False
    except RuntimeError:
        assert True