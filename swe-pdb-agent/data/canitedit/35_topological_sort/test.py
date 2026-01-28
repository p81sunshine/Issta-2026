from solution import *
import math

def test_all():
    n1 = Node(1, [2])
    n2 = Node(2, [3])
    n3 = Node(3, [1])    

    n4 = Node(3, [])
    n5 = Node(4, [2])
    n6 = Node(5, [4, 1])

    cyclic = Graph([n1, n2, n3])
    dag = Graph([n1, n2, n4, n5, n6])
    sorted_dag = dag.topological_sort()

    n7 = Node(7, [8, 9, 10, 11])
    n8 = Node(8, [12])
    n9 = Node(9, [])
    n10 = Node(10, [])
    n11 = Node(11, [13])
    n12 =  Node(12, [])
    n13 = Node(13, [])

    legal_sortings_2 = Graph([n7, n8, n9, n10, n11, n12, n13])
    sorted_dag_2 = legal_sortings_2.topological_sort()

    try:
        Node(1, [2, 2])
        assert False
    except:
        assert True

    try:
        Graph([n1, n1])
        assert False
    except:
        assert True

    try:
        cyclic.topological_sort()
        assert False
    except:
        assert True 

    assert cyclic.find_node(1) == n1
    assert sorted_dag[0] == n6
    assert sorted_dag[1] == n1
    assert sorted_dag[2] == n5
    assert sorted_dag[3] == n2
    assert sorted_dag[4] == n4

    def node_before_other(one: Node, two: Node, dag: List[Node]):
        found_first = False
        for node in dag:
            if node == one:
                found_first = True
            if node == two:
                if found_first:
                    return True
                else:
                    return False

    assert sorted_dag_2[0] == n7
    assert node_before_other(n8, n12, sorted_dag_2)
    assert node_before_other(n11, n13, sorted_dag_2)