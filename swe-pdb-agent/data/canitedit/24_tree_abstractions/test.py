from solution import *
import math

def test_all():
    add_ten = lambda e : e + 10
    is_positive = lambda e : e > 0
    contains_x = lambda e : "x" in e
    count_length = lambda e : len(e)

    assert Leaf(3).tree_map(add_ten).value == Leaf(13).value
    assert Leaf(-10).tree_andmap(is_positive) == False

    assert Leaf("hello").tree_filter(contains_x, 0).value == "hello"

    tree = Node(Node(Leaf(2), Node(Leaf(5), Leaf(11))), Node(Leaf(7), Leaf(6)))
    assert tree.tree_map(add_ten) == Node(Node(Leaf(12), Node(Leaf(15), Leaf(21))), Node(Leaf(17), Leaf(16)))
    assert tree.tree_filter(is_positive, 0) == Node(Node(Leaf(0), Node(Leaf(0), Leaf(0))), Node(Leaf(0), Leaf(0)))

    assert Node(Leaf(10), Node(Leaf(4), Leaf(-9))).tree_andmap(is_positive) == False
    assert Node(Leaf(10), Node(Leaf(4), Leaf(-9))).tree_ormap(is_positive) == True

    tree2 = Node(Node(Leaf("hello"), Leaf("world")), Node(Node(Node(Leaf("hx"), Leaf("ow")), Leaf("owaowa")), Leaf("epa")))

    assert tree2.tree_map(count_length) == Node(Node(Leaf(5), Leaf(5)), Node(Node(Node(Leaf(2), Leaf(2)), Leaf(6)), Leaf(3)))
    assert tree2.tree_ormap(contains_x) == True
    assert tree2.tree_andmap(contains_x) == False

    assert tree2 != 2
    assert Leaf(3) != Leaf(4)
    assert Leaf(3) != 1