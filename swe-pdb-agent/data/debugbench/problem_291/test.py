from solution import *

def test_example_1():
    recipes = ["bread"]
    ingredients = [["yeast","flour"]]
    supplies = ["yeast","flour","corn"]
    expected = ["bread"]
    assert findAllRecipes(recipes, ingredients, supplies) == expected

def test_example_2():
    recipes = ["bread","sandwich"]
    ingredients = [["yeast","flour"],["bread","meat"]]
    supplies = ["yeast","flour","meat"]
    expected = ["bread","sandwich"]
    assert findAllRecipes(recipes, ingredients, supplies) == expected

def test_example_3():
    recipes = ["bread","sandwich","burger"]
    ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]]
    supplies = ["yeast","flour","meat"]
    expected = ["bread","sandwich","burger"]
    assert findAllRecipes(recipes, ingredients, supplies) == expected

def test_unreachable_recipe():
    recipes = ["cake"]
    ingredients = [["flour", "eggs"]]
    supplies = ["flour"]
    expected = []
    assert findAllRecipes(recipes, ingredients, supplies) == expected

def test_chained_recipes():
    recipes = ["A", "B"]
    ingredients = [["X"], ["A", "Y"]]
    supplies = ["X", "Y"]
    expected = ["A", "B"]
    assert findAllRecipes(recipes, ingredients, supplies) == expected