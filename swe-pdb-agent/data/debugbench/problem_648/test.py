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

def test_cycle_dependency():
    recipes = ["cake", "icing"]
    ingredients = [["icing"], ["cake"]]
    supplies = []
    expected = []
    assert findAllRecipes(recipes, ingredients, supplies) == expected

def test_empty_input():
    assert findAllRecipes([], [], []) == []