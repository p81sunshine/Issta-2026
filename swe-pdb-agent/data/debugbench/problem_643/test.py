from solution import *

def test_example_1():
    assert findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"], ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]) == ["Shogun"], "Should return ['Shogun']"

def test_example_2():
    assert findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"], ["KFC","Shogun","Burger King"]) == ["Shogun"], "Should return ['Shogun']"

def test_example_3():
    result = findRestaurant(["happy","sad","good"], ["sad","happy","good"])
    assert set(result) == {"sad", "happy"}, "Should return both 'sad' and 'happy' regardless of order"

def test_edge_case_single_match():
    assert findRestaurant(["a"], ["a"]) == ["a"], "Should return ['a'] for single match"

def test_edge_case_multiple_equal_sums():
    # Buggy code would fail here because it starts from index 1 instead of 0
    assert findRestaurant(["a","b"], ["b","a"]) == ["a","b"], "Should return ['a','b'] when sums are equal"