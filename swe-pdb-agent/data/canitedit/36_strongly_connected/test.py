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
    scc = g.strongly_connected_components()

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

    assert scc[n1] == scc[n2] and scc[n1] == scc[n3]
    assert scc[n4] != scc[n1] and scc[n4] != scc[n2] and scc[n4] != scc[n3]

    assert Node(1) == Node(1)
    assert Node(1) != Node(2)
    assert Node(1) != 1

    # test for RuntimeError in Graph.__init__
    try:
        Graph([Node(1), Node(1)])
        assert False
    except RuntimeError:
        assert True