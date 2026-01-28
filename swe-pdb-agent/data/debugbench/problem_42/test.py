from solution import *

def test_example_1():
    recipes = ["bread"]
    ingredients = [["yeast","flour"]]
    supplies = ["yeast","flour","corn"]
    expected = ["bread"]
    actual = find_all_recipes(recipes, ingredients, supplies)
    assert actual == expected, f"Expected {expected} but got {actual}"

def test_example_2():
    recipes = ["bread","sandwich"]
    ingredients = [["yeast","flour"],["bread","meat"]]
    supplies = ["yeast","flour","meat"]
    expected = ["bread","sandwich"]
    actual = find_all_recipes(recipes, ingredients, supplies)
    assert actual == expected, f"Expected {expected} but got {actual}"

def test_example_3():
    recipes = ["bread","sandwich","burger"]
    ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]]
    supplies = ["yeast","flour","meat"]
    expected = ["bread","sandwich","burger"]
    actual = find_all_recipes(recipes, ingredients, supplies)
    assert actual == expected, f"Expected {expected} but got {actual}"

def test_cycle_dependency():
    recipes = ["A", "B"]
    ingredients = [["B"], ["A"]]
    supplies = []
    expected = []
    actual = find_all_recipes(recipes, ingredients, supplies)
    assert actual == expected, "Cycle should return empty list"

def test_missing_ingredient():
    recipes = ["cake"]
    ingredients = [["flour", "eggs"]]
    supplies = ["flour"]
    expected = []
    actual = find_all_recipes(recipes, ingredients, supplies)
    assert actual == expected, "Missing eggs should prevent cake creation"

def test_dependency_chain():
    recipes = ["A", "B", "C"]
    ingredients = [["X"], ["A", "Y"], ["B", "Z"]]
    supplies = ["X", "Y", "Z"]
    expected = ["A", "B", "C"]
    actual = find_all_recipes(recipes, ingredients, supplies)
    assert actual == expected, "All recipes in dependency chain should be created"