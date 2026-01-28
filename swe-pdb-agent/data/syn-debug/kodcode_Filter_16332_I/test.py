from solution import *

import math

from solution import *

import math

from solution import *

import math

import pytest
from unittest.mock import patch
from solution import QuizGame


def test_add_question():
    game = QuizGame()
    with patch('builtins.input', side_effect=["What is 2 + 2?", "4"]):
        game.add_question()
    assert game.questions == {"What is 2 + 2?": "4"}

def test_view_high_score():
    game = QuizGame()
    game.high_score = 5
    with patch('builtins.print') as mock_print:
        game.view_high_score()
        mock_print.assert_called_with("High Score: 5")

def test_start_quiz_correct_answer():
    game = QuizGame()
    game.questions = {"What is the capital of France?": "Paris"}
    with patch('builtins.input', side_effect=["Paris"]):
        with patch('builtins.print') as mock_print:
            game.start_quiz()
            assert game.high_score == 1
            mock_print.assert_any_call("Correct!")
            mock_print.assert_any_call("Your current score is 1")

def test_start_quiz_incorrect_answer():
    game = QuizGame()
    game.questions = {"What is the capital of France?": "Paris"}
    with patch('builtins.input', side_effect=["London"]):
        with patch('builtins.print') as mock_print:
            game.start_quiz()
            assert game.high_score == 0
            mock_print.assert_any_call("Wrong! The correct answer is 'Paris'")
            mock_print.assert_any_call("Your current score is 0")

def test_start_quiz_with_no_questions():
    game = QuizGame()
    with patch('builtins.print') as mock_print:
        game.start_quiz()
        mock_print.assert_called_with("No questions available. Please add questions first.")

def test_menu_exit():
    game = QuizGame()
    with patch('builtins.input', side_effect=['4']):
        assert game.menu() is None # Returns None when Exit is selected