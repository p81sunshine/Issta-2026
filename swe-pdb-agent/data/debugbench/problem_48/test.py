from solution import *

def test_example_1():
    list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
    list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
    assert findRestaurant(list1, list2) == ["Shogun"], "Example 1 failed"

def test_example_2():
    list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
    list2 = ["KFC","Shogun","Burger King"]
    assert findRestaurant(list1, list2) == ["Shogun"], "Example 2 failed"

def test_example_3():
    list1 = ["happy","sad","good"]
    list2 = ["sad","happy","good"]
    result = findRestaurant(list1, list2)
    assert set(result) == {"sad", "happy"}, "Example 3 failed"

def test_tie_with_multiple_entries():
    list1 = ["a", "b", "c"]
    list2 = ["c", "b", "a"]
    result = findRestaurant(list1, list2)
    assert set(result) == {"a", "b", "c"}, "Multiple tie case failed"