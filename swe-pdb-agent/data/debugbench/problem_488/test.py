from solution import *

def test_example_1():
    recipes = ["bread"]
    ingredients = [["yeast","flour"]]
    supplies = ["yeast","flour","corn"]
    expected = ["bread"]
    result = findAllRecipes(recipes, ingredients, supplies)
    assert result == expected, f"Expected {expected} but got {result}"

def test_example_2():
    recipes = ["bread","sandwich"]
    ingredients = [["yeast","flour"],["bread","meat"]]
    supplies = ["yeast","flour","meat"]
    expected = ["bread","sandwich"]
    result = findAllRecipes(recipes, ingredients, supplies)
    assert result == expected, f"Expected {expected} but got {result}"

def test_example_3():
    recipes = ["bread","sandwich","burger"]
    ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]]
    supplies = ["yeast","flour","meat"]
    expected = ["bread","sandwich","burger"]
    result = findAllRecipes(recipes, ingredients, supplies)
    assert result == expected, f"Expected {expected} but got {result}"

def test_no_possible_recipes():
    recipes = ["cake"]
    ingredients = [["flour", "sugar"]]
    supplies = ["flour"]
    expected = []
    result = findAllRecipes(recipes, ingredients, supplies)
    assert result == expected, "Should return empty list when ingredients not fully available"

def test_circular_dependency():
    recipes = ["A", "B"]
    ingredients = [["B"], ["A"]]
    supplies = []
    expected = []
    result = findAllRecipes(recipes, ingredients, supplies)
    assert result == expected, "Circular dependency should result in no recipes"