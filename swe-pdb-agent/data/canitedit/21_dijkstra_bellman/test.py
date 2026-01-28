from solution import *
import math

def test_all():
    graph1 = Graph()
    for node in ['A', 'B', 'C', 'D']:
        graph1.add_node(node)
    graph1.add_edge('A', 'B', 1)
    graph1.add_edge('B', 'C', 2)
    graph1.add_edge('C', 'D', 3)
    graph1.add_edge('A', 'D', 10)

    shortest_path1 = graph1.distances_to('A')
    assert shortest_path1 == {'A': 0, 'B': 1, 'C': 3, 'D': 6}, "Test 1 failed!"

    graph2 = Graph()
    for node in ['A', 'B', 'C', 'D']:
        graph2.add_node(node)
    graph2.add_edge('A', 'B', 1)
    graph2.add_edge('B', 'C', 2)
    graph2.add_edge('C', 'D', -5)
    graph2.add_edge('A', 'D', 2)

    shortest_path2 = graph2.distances_to('A')
    assert shortest_path2 == {'A': 0, 'B': 1,
                              'C': 3, 'D': -2}, "Test 2 failed!"

    graph3 = Graph()
    for node in ['A', 'B', 'C', 'D']:
        graph3.add_node(node)
    graph3.add_edge('A', 'B', 1)
    graph3.add_edge('B', 'C', 2)
    graph3.add_edge('C', 'A', -4)  # Negative cycle: A -> B -> C -> A
    graph3.add_edge('C', 'D', 2)

    try:
        shortest_path3 = graph3.distances_to('A')
    except:
        pass
    else:
        assert False, "Test 3 failed: no exception was raised for a negative cycle"

    graph4 = Graph()
    try:
        shortest_path4 = graph4.distances_to('A')
    except:
        pass  # Expected, since 'A' is not in the graph
    else:
        assert False, "Test 4 failed: No exception raised for empty graph"

    graph5 = Graph()
    graph5.add_node('A')
    shortest_path5 = graph5.distances_to('A')
    assert shortest_path5 == {
        'A': 0}, "Test 5 failed: Graph with one node should have distance 0 to itself"

    graph6 = Graph()
    for node in ['A', 'B', 'C']:
        graph6.add_node(node)
    # No edges added, so B and C should remain at infinity
    shortest_path6 = graph6.distances_to('A')
    assert shortest_path6 == {'A': 0, 'B': float('infinity'), 'C': float(
        'infinity')}, "Test 6 failed: Disconnected nodes should have infinite distance"

    graph7 = Graph()
    for node in ['A', 'B', 'C']:
        graph7.add_node(node)
    graph7.add_edge('A', 'B', 0)
    graph7.add_edge('B', 'C', 0)
    shortest_path7 = graph7.distances_to('A')
    assert shortest_path7 == {
        'A': 0, 'B': 0, 'C': 0}, "Test 7 failed: Zero-weight edges should not add to the distance"

    graph8 = Graph()
    for node in ['A', 'B']:
        graph8.add_node(node)
    graph8.add_edge('A', 'A', -1)  # Self-loop with negative weight
    graph8.add_edge('A', 'B', 2)
    try:
        shortest_path8 = graph8.distances_to('A')
    except:
        pass
    else:
        assert False, "Test 8 failed: no exception was raised for negative self-loop"

    graph9 = Graph()
    for node in ['A', 'B']:
        graph9.add_node(node)
    graph9.add_edge('A', 'B', 1)
    try:
        shortest_path9 = graph9.distances_to('C')
    except:
        pass  # Expected, since 'C' is not in the graph
    else:
        assert False, "Test 9 failed: No exception raised for non-existent start node"

    graph10 = Graph()
    for node in ['A', 'B', 'C', 'D']:
        graph10.add_node(node)
    graph10.add_edge('A', 'B', 2)
    graph10.add_edge('B', 'C', -1)
    graph10.add_edge('C', 'D', 2)
    graph10.add_edge('A', 'D', 10)
    shortest_path10 = graph10.distances_to('A')
    assert shortest_path10 == {'A': 0, 'B': 2, 'C': 1,
                               'D': 3}, "Test 10 failed: Path with negative weight not calculated correctly"

    graph11 = Graph()
    for node in ['A', 'B', 'C', 'D', 'E', 'F']:
        graph11.add_node(node)
    graph11.add_edge('A', 'B', 5)
    graph11.add_edge('A', 'C', 2)
    graph11.add_edge('B', 'D', -3)
    graph11.add_edge('C', 'E', 6)
    graph11.add_edge('D', 'F', 1)
    graph11.add_edge('E', 'D', -2)
    graph11.add_edge('F', 'E', -1)

    try:
        shortest_path11 = graph11.distances_to('A')
    except:
        pass
    else:
        assert False, "Test 11 failed: No exception raised for negative cycle"

    graph12 = Graph()
    for node in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
        graph12.add_node(node)
    graph12.add_edge('A', 'B', 4)
    graph12.add_edge('A', 'C', 3)
    graph12.add_edge('B', 'C', 1)
    graph12.add_edge('B', 'D', 2)
    graph12.add_edge('C', 'D', 4)
    graph12.add_edge('C', 'E', 2)
    graph12.add_edge('D', 'F', -1)
    graph12.add_edge('E', 'F', -2)
    graph12.add_edge('E', 'G', 1)
    graph12.add_edge('F', 'G', 2)

    shortest_path12 = graph12.distances_to('A')
    assert shortest_path12 == {
        'A': 0,
        'B': 4,
        'C': 3,
        'D': 6,
        'E': 5,
        'F': 3,
        'G': 5
    }, "Test 12 failed: Complex graph without a negative cycle not calculated correctly"