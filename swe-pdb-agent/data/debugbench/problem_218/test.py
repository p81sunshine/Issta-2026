from solution import *

def test_example_1():
    list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
    list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
    expected = ["Shogun"]
    actual = findRestaurant(list1, list2)
    assert actual == expected, "Example 1 failed"

def test_example_2():
    list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
    list2 = ["KFC","Shogun","Burger King"]
    expected = ["Shogun"]
    actual = findRestaurant(list1, list2)
    assert actual == expected, "Example 2 failed"

def test_example_3():
    list1 = ["happy","sad","good"]
    list2 = ["sad","happy","good"]
    expected = ["sad", "happy"]
    actual = findRestaurant(list1, list2)
    assert sorted(actual) == sorted(expected), "Example 3 failed"

def test_all_same_sum():
    list1 = ["a", "b", "c"]
    list2 = ["c", "b", "a"]
    expected = ["a", "b", "c"]
    actual = findRestaurant(list1, list2)
    assert sorted(actual) == sorted(expected), "All same sum test failed"

def test_minimum_sum_only():
    list1 = ["a", "b"]
    list2 = ["a", "b"]
    expected = ["a"]
    actual = findRestaurant(list1, list2)
    assert actual == expected, "Minimum sum only test failed"