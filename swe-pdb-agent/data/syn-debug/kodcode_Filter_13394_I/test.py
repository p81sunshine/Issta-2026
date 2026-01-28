from solution import *

import math

from solution import *

import math

from solution import *

import math

from solution import AnimalShelterGame

def test_adopt_cat():
    game = AnimalShelterGame()
    assert game.adopt("cat") == "You have adopted a cat."
    assert game.balance == 80
    assert game.adopted_animals == ["cat"]

def test_adopt_dog():
    game = AnimalShelterGame()
    assert game.adopt("dog") == "You have adopted a dog."
    assert game.balance == 50
    assert game.adopted_animals == ["dog"]

def test_adopt_fish():
    game = AnimalShelterGame()
    assert game.adopt("fish") == "You have adopted a fish."
    assert game.balance == 90
    assert game.adopted_animals == ["fish"]

def test_insufficient_balance():
    game = AnimalShelterGame()
    game.balance = 30
    assert game.adopt("dog") == "You don't have enough money to adopt this animal."
    assert game.balance == 30
    assert game.adopted_animals == []

def test_invalid_animal():
    game = AnimalShelterGame()
    assert game.adopt("rabbit") == "Invalid animal choice."
    assert game.balance == 100
    assert game.adopted_animals == []

def test_view_balance_and_adopted_animals():
    game = AnimalShelterGame()
    game.adopt("dog")
    assert game.view_balance_and_adopted_animals() == {"balance": 50, "adopted_animals": ["dog"]}

def test_quit_game():
    game = AnimalShelterGame()
    assert game.quit_game() == "Game Over. Thank you for playing!"