import pytest
from acecode_oss_3019_codellama_instruct_13_code import determine_winner

def test_case_0():
    assert determine_winner('rock', 'rock') == "It's a tie"

def test_case_1():
    assert determine_winner('rock', 'paper') == "Computer wins"

def test_case_2():
    assert determine_winner('rock', 'scissors') == "User wins"

def test_case_3():
    assert determine_winner('paper', 'rock') == "User wins"

def test_case_4():
    assert determine_winner('paper', 'paper') == "It's a tie"

def test_case_5():
    assert determine_winner('paper', 'scissors') == "Computer wins"

def test_case_6():
    assert determine_winner('scissors', 'rock') == "Computer wins"

def test_case_7():
    assert determine_winner('scissors', 'paper') == "User wins"

def test_case_8():
    assert determine_winner('scissors', 'scissors') == "It's a tie"

def test_case_9():
    assert determine_winner('rock', 'rock') == "It's a tie"

def test_case_10():
    assert determine_winner('rock', 'scissors') == "User wins"

def test_case_11():
    assert determine_winner('paper', 'scissors') == "Computer wins"

def test_case_12():
    assert determine_winner('scissors', 'rock') == "Computer wins"

def test_case_13():
    assert determine_winner('rock', 'paper') == "Computer wins"

def test_case_14():
    assert determine_winner('paper', 'rock') == "User wins"

def test_case_15():
    assert determine_winner('scissors', 'scissors') == "It's a tie"

def test_case_16():
    assert determine_winner('rock', 'paper') == "Computer wins"

def test_case_17():
    assert determine_winner('paper', 'paper') == "It's a tie"

def test_case_18():
    assert determine_winner('scissors', 'paper') == "User wins"

def test_case_19():
    assert determine_winner('rock', 'scissors') == "User wins"