import pytest
from acecode_bigcode_python_fns_29604_llama3_1_instruct_40_code import is_valid

def test_case_0():
    assert is_valid({'name': 'Alice', 'age': 30, 'is_student': False}, {'name': 'string', 'age': 'integer', 'is_student': 'boolean'}) == True

def test_case_1():
    assert is_valid({'name': 'Bob', 'age': '25', 'is_student': True}, {'name': 'string', 'age': 'integer', 'is_student': 'boolean'}) == False

def test_case_2():
    assert is_valid({'name': 'Charlie', 'is_student': True}, {'name': 'string', 'age': 'integer', 'is_student': 'boolean'}) == False

def test_case_3():
    assert is_valid({'name': 'Diana', 'age': 22}, {'name': 'string', 'age': 'integer', 'is_student': 'boolean'}) == False

def test_case_4():
    assert is_valid({'name': 123, 'age': 25, 'is_student': False}, {'name': 'string', 'age': 'integer', 'is_student': 'boolean'}) == False

def test_case_5():
    assert is_valid({'name': 'Eve', 'age': 25, 'is_student': True}, {'name': 'string', 'age': 'integer', 'is_student': 'boolean'}) == True

def test_case_6():
    assert is_valid({}, {'name': 'string', 'age': 'integer'}) == False

def test_case_7():
    assert is_valid({'name': 'Frank', 'age': 40, 'is_student': None}, {'name': 'string', 'age': 'integer', 'is_student': 'boolean'}) == False

def test_case_8():
    assert is_valid({'name': 'Grace', 'age': 28, 'is_student': True}, {'name': 'string', 'age': 'integer', 'is_student': 'boolean'}) == True

def test_case_9():
    assert is_valid({'name': 'Hannah', 'age': 20, 'is_student': 'yes'}, {'name': 'string', 'age': 'integer', 'is_student': 'boolean'}) == False

def test_case_10():
    assert is_valid({'name': 'Igor', 'age': 33}, {'name': 'string', 'age': 'integer', 'is_student': 'boolean'}) == False

def test_case_11():
    assert is_valid({'name': 'Jack', 'age': 29, 'is_student': True}, {'name': 'string', 'age': 'integer', 'is_student': 'boolean'}) == True

def test_case_12():
    assert is_valid({'name': 'Kathy', 'age': 'unknown'}, {'name': 'string', 'age': 'integer'}) == False

def test_case_13():
    assert is_valid({'name': 'Leo', 'age': 35, 'is_student': False}, {'name': 'string', 'age': 'integer', 'is_student': 'boolean'}) == True

def test_case_14():
    assert is_valid({'name': 'Mona', 'age': 30, 'is_student': 'no'}, {'name': 'string', 'age': 'integer', 'is_student': 'boolean'}) == False

def test_case_15():
    assert is_valid({'name': 'Nate'}, {'name': 'string', 'age': 'integer'}) == False

def test_case_16():
    assert is_valid({'name': 'Owen', 'age': 22, 'is_student': False}, {'name': 'string', 'age': 'integer', 'is_student': 'boolean'}) == True

def test_case_17():
    assert is_valid({'name': 'Paula', 'age': 27, 'is_student': True}, {'name': 'string', 'age': 'integer', 'is_student': 'boolean'}) == True

def test_case_18():
    assert is_valid({'name': 'Quinn', 'age': 19}, {'name': 'string', 'age': 'integer', 'is_student': 'boolean'}) == False

def test_case_19():
    assert is_valid({'name': 'Rita', 'age': 31, 'is_student': False}, {'name': 'string', 'age': 'integer', 'is_student': 'boolean'}) == True