from solution import *

def test_example_1():
    recipes = ["bread"]
    ingredients = [["yeast","flour"]]
    supplies = ["yeast","flour","corn"]
    expected = ["bread"]
    result = find_all_recipes(recipes, ingredients, supplies)
    assert result == expected, f"Expected {expected}, but got {result}"

def test_example_2():
    recipes = ["bread","sandwich"]
    ingredients = [["yeast","flour"],["bread","meat"]]
    supplies = ["yeast","flour","meat"]
    expected = ["bread","sandwich"]
    result = find_all_recipes(recipes, ingredients, supplies)
    assert result == expected, f"Expected {expected}, but got {result}"

def test_example_3():
    recipes = ["bread","sandwich","burger"]
    ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]]
    supplies = ["yeast","flour","meat"]
    expected = ["bread","sandwich","burger"]
    result = find_all_recipes(recipes, ingredients, supplies)
    assert result == expected, f"Expected {expected}, but got {result}"

def test_cycle():
    recipes = ["a", "b"]
    ingredients = [["b"], ["a"]]
    supplies = []
    expected = []
    result = find_all_recipes(recipes, ingredients, supplies)
    assert result == expected, f"Expected {expected}, but got {result}"

def test_partial_supplies():
    recipes = ["cake"]
    ingredients = [["flour", "eggs"]]
    supplies = ["flour"]
    expected = []
    result = find_all_recipes(recipes, ingredients, supplies)
    assert result == expected, f"Expected {expected}, but got {result}"