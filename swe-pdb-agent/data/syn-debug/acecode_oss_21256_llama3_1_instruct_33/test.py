import pytest
from acecode_oss_21256_llama3_1_instruct_33_code import validate_duration

def test_case_0():
    assert validate_duration('P1Y2M3DT4H5M6S', ['P1Y2M3DT4H5M6S', 'P2Y3M4DT5H6M7S', 'P3Y4M5DT6H7M8S']) == True

def test_case_1():
    assert validate_duration('P2Y3M4DT5H6M7S', ['P1Y2M3DT4H5M6S', 'P2Y3M4DT5H6M7S', 'P3Y4M5DT6H7M8S']) == True

def test_case_2():
    assert validate_duration('P3Y4M5DT6H7M8S', ['P1Y2M3DT4H5M6S', 'P2Y3M4DT5H6M7S', 'P3Y4M5DT6H7M8S']) == True

def test_case_3():
    assert validate_duration('P4Y5M6DT7H8M9S', ['P1Y2M3DT4H5M6S', 'P2Y3M4DT5H6M7S', 'P3Y4M5DT6H7M8S']) == False

def test_case_4():
    assert validate_duration('P1Y0M0DT0H0M0S', ['P1Y0M0DT0H0M0S']) == True

def test_case_5():
    assert validate_duration('P0Y0M0DT0H0M0S', ['P0Y0M0DT0H0M0S']) == True

def test_case_6():
    assert validate_duration('P1Y2M3DT0H0M0S', ['P1Y2M3DT0H0M0S', 'P3Y4M5DT6H7M8S']) == True

def test_case_7():
    assert validate_duration('P1Y2M3DT4H5M6S', ['P1Y2M3DT4H5M6S', 'P1Y2M3DT4H5M7S']) == True

def test_case_8():
    assert validate_duration('P1Y2M3DT4H5M6S', ['P1Y2M3DT4H5M6S', 'P1Y2M3DT4H5M8S']) == True

def test_case_9():
    assert validate_duration('P1Y2M3DT4H5M6S', ['P1Y2M3DT4H5M6S', 'P1Y2M3DT4H6M6S']) == True

def test_case_10():
    assert validate_duration('P2Y3M4DT5H6M7S', ['P2Y3M4DT5H6M7S', 'P2Y3M4DT5H6M8S']) == True

def test_case_11():
    assert validate_duration('P3Y4M5DT6H7M8S', ['P3Y4M5DT6H7M8S', 'P3Y4M5DT6H7M9S']) == True

def test_case_12():
    assert validate_duration('P4Y5M6DT7H8M9S', ['P4Y5M6DT7H8M9S', 'P4Y5M6DT7H8M8S']) == True

def test_case_13():
    assert validate_duration('P5Y6M7DT8H9M10S', ['P5Y6M7DT8H9M10S']) == True

def test_case_14():
    assert validate_duration('P1Y2M3DT4H5M7S', ['P1Y2M3DT4H5M6S']) == False

def test_case_15():
    assert validate_duration('P1Y2M3DT4H5M6S', ['P1Y2M3DT4H5M6S', 'P1Y2M3DT4H5M6S']) == True

def test_case_16():
    assert validate_duration('P1Y2M3DT4H5M6S', ['P1Y2M3DT4H5M6S', 'P1Y2M3DT4H5M9S']) == True

def test_case_17():
    assert validate_duration('P1Y2M3DT4H5M6S', ['P1Y2M3DT4H5M6S', 'P1Y2M3DT4H5M7S']) == True

def test_case_18():
    assert validate_duration('P2Y3M4DT5H6M7S', ['P2Y3M4DT5H6M7S', 'P2Y3M4DT5H6M6S']) == True

def test_case_19():
    assert validate_duration('P3Y4M5DT6H7M8S', ['P3Y4M5DT6H7M8S']) == True

def test_case_20():
    assert validate_duration('P4Y5M6DT7H8M9S', ['P3Y4M5DT6H7M8S', 'P4Y5M6DT7H8M9S']) == True