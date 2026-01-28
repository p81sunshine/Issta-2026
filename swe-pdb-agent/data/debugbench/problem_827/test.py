from solution import *

def test_example_1():
    recipes = ["bread"]
    ingredients = [["yeast","flour"]]
    supplies = ["yeast","flour","corn"]
    expected = ["bread"]
    result = findAllRecipes(recipes, ingredients, supplies)
    assert result == expected, "Example 1 failed"

def test_example_2():
    recipes = ["bread","sandwich"]
    ingredients = [["yeast","flour"],["bread","meat"]]
    supplies = ["yeast","flour","meat"]
    expected = ["bread","sandwich"]
    result = findAllRecipes(recipes, ingredients, supplies)
    assert result == expected, "Example 2 failed"

def test_example_3():
    recipes = ["bread","sandwich","burger"]
    ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]]
    supplies = ["yeast","flour","meat"]
    expected = ["bread","sandwich","burger"]
    result = findAllRecipes(recipes, ingredients, supplies)
    assert result == expected, "Example 3 failed"

def test_cycle_dependency():
    recipes = ["A", "B"]
    ingredients = [["B"], ["A"]]
    supplies = []
    expected = []
    result = findAllRecipes(recipes, ingredients, supplies)
    assert result == expected, "Cycle dependency should return empty list"

def test_missing_supply():
    recipes = ["cake"]
    ingredients = [["flour", "sugar"]]
    supplies = ["flour"]
    expected = []
    result = findAllRecipes(recipes, ingredients, supplies)
    assert result == expected, "Missing supply should return empty list"