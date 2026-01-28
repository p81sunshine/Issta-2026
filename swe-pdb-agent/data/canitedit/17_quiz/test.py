from solution import *
import math

def test_all():
    questions = ["How many days in a week?", "What color absorbs the most light?",
                 "Which language has more native speakers? English or Spanish?", "Who has won the most academy awards?"]
    answers = ["7", "Black", "Spanish", "Walt Disney"]

    quiz = Quiz(questions, answers)

    assert quiz.score == 0
    assert quiz.current_question == 0
    assert quiz.skipped == 0

    assert quiz.check_answer(0, "7")
    q = quiz.next_question()
    assert q == "How many days in a week?"

    assert quiz.score == 1
    assert quiz.current_question == 1
    assert quiz.skipped == 0

    quiz.skip_question()

    assert quiz.score == 1
    assert quiz.current_question == 2
    assert quiz.skipped == 1

    assert "skip" in quiz.display_results().lower()

    q = quiz.next_question()
    assert not quiz.check_answer(1, "Walt Disney")
    assert q == "Which language has more native speakers? English or Spanish?"

    quiz.next_question()
    try:
        quiz.next_question()
        assert False, "Should have raised IndexError"
    except IndexError:
        pass

    quiz.add_question("What is the capital of Nigeria?", "Abuja")
    assert quiz.total_questions == 5
    assert quiz.answers[-1] == "Abuja"
    q = quiz.next_question()
    assert q == "What is the capital of Nigeria?"
    assert quiz.check_answer(4, "Abuja")