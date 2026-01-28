from solution import *

def test_example_1():
    names = ["pes","fifa","gta","pes(2019)"]
    expected = ["pes","fifa","gta","pes(2019)"]
    assert getFolderNames(names) == expected, "Example 1 failed"

def test_example_2():
    names = ["gta","gta(1)","gta","avalon"]
    expected = ["gta","gta(1)","gta(2)","avalon"]
    assert getFolderNames(names) == expected, "Example 2 failed"

def test_example_3():
    names = ["onepiece","onepiece(1)","onepiece(2)","onepiece(3)","onepiece"]
    expected = ["onepiece","onepiece(1)","onepiece(2)","onepiece(3)","onepiece(4)"]
    assert getFolderNames(names) == expected, "Example 3 failed"

def test_edge_case_1():
    names = ["a", "a", "a"]
    expected = ["a", "a(1)", "a(2)"]
    assert getFolderNames(names) == expected, "Edge case 1 failed"

def test_edge_case_2():
    names = ["a", "a(1)", "a"]
    expected = ["a", "a(1)", "a(2)"]
    assert getFolderNames(names) == expected, "Edge case 2 failed"