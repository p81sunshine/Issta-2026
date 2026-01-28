from solution import *

def test_example_1():
    recipes = ["bread"]
    ingredients = [["yeast","flour"]]
    supplies = ["yeast","flour","corn"]
    expected = ["bread"]
    actual = findAllRecipes(recipes, ingredients, supplies)
    assert actual == expected, f"Expected {expected} but got {actual}"

def test_example_2():
    recipes = ["bread","sandwich"]
    ingredients = [["yeast","flour"],["bread","meat"]]
    supplies = ["yeast","flour","meat"]
    expected = ["bread","sandwich"]
    actual = findAllRecipes(recipes, ingredients, supplies)
    assert actual == expected, f"Expected {expected} but got {actual}"

def test_example_3():
    recipes = ["bread","sandwich","burger"]
    ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]]
    supplies = ["yeast","flour","meat"]
    expected = ["bread","sandwich","burger"]
    actual = findAllRecipes(recipes, ingredients, supplies)
    assert actual == expected, f"Expected {expected} but got {actual}"

def test_index_error_bug():
    recipes = ["cake"]
    ingredients = [["flour"]]
    supplies = ["flour"]
    expected = ["cake"]
    actual = findAllRecipes(recipes, ingredients, supplies)
    assert actual == expected, f"Expected {expected} but got {actual}"

def test_unavailable_ingredient():
    recipes = ["cake"]
    ingredients = [["flour", "sugar"]]
    supplies = ["flour"]
    expected = []
    actual = findAllRecipes(recipes, ingredients, supplies)
    assert actual == expected, f"Expected {expected} but got {actual}"