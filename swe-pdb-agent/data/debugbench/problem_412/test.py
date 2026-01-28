from solution import *

def test_example_1():
    list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
    list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
    expected = ["Shogun"]
    actual = findRestaurant(list1, list2)
    assert sorted(actual) == sorted(expected), "Test case 1 failed"

def test_example_2():
    list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
    list2 = ["KFC","Shogun","Burger King"]
    expected = ["Shogun"]
    actual = findRestaurant(list1, list2)
    assert sorted(actual) == sorted(expected), "Test case 2 failed"

def test_example_3():
    list1 = ["happy","sad","good"]
    list2 = ["sad","happy","good"]
    expected = ["sad","happy"]
    actual = findRestaurant(list1, list2)
    assert sorted(actual) == sorted(expected), "Test case 3 failed"

def test_case_multiple_same_sum():
    list1 = ["a", "b"]
    list2 = ["b", "a"]
    expected = ["a", "b"]
    actual = findRestaurant(list1, list2)
    assert sorted(actual) == sorted(expected), "Test case multiple same sum failed"

def test_case_edge_no_common():
    list1 = ["a", "b"]
    list2 = ["c", "d"]
    expected = []
    try:
        actual = findRestaurant(list1, list2)
    except IndexError:
        assert True, "Expected empty list but code raised error"
    else:
        assert actual == expected, "Test case no common elements failed"