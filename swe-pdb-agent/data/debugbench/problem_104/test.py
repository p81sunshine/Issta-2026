from solution import *

def test_example_1():
    input = ["pes","fifa","gta","pes(2019)"]
    expected = ["pes","fifa","gta","pes(2019)"]
    assert getFolderNames(input) == expected, "Failed for example 1"

def test_example_2():
    input = ["gta","gta(1)","gta","avalon"]
    expected = ["gta","gta(1)","gta(2)","avalon"]
    assert getFolderNames(input) == expected, "Failed for example 2"

def test_example_3():
    input = ["onepiece","onepiece(1)","onepiece(2)","onepiece(3)","onepiece"]
    expected = ["onepiece","onepiece(1)","onepiece(2)","onepiece(3)","onepiece(4)"]
    assert getFolderNames(input) == expected, "Failed for example 3"

def test_edge_case_duplicate_chain():
    input = ["a", "a", "a", "a"]
    expected = ["a", "a(1)", "a(2)", "a(3)"]
    assert getFolderNames(input) == expected, "Failed for duplicate chain"

def test_edge_case_nested_suffix():
    input = ["a(1)", "a(1)", "a(1)"]
    expected = ["a(1)", "a(1)(1)", "a(1)(2)"]
    assert getFolderNames(input) == expected, "Failed for nested suffix handling"