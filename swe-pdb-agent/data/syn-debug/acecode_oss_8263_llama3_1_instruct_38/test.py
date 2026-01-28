import pytest
from acecode_oss_8263_llama3_1_instruct_38_code import parse_simulation_config

def test_case_0():
    assert parse_simulation_config(['Verbosity = 0', 'firstRun = 1', 'maxEvents = 10', 'UseMagneticField = True']) == {'Verbosity': 0, 'firstRun': 1, 'maxEvents': 10, 'UseMagneticField': True}

def test_case_1():
    assert parse_simulation_config(['UseMagneticField = False', 'maxEvents = 5', 'firstRun = 2', 'Verbosity = 1']) == {'Verbosity': 1, 'firstRun': 2, 'maxEvents': 5, 'UseMagneticField': False}

def test_case_2():
    assert parse_simulation_config(['firstRun = 0', 'maxEvents = 100', 'Verbosity = 2', 'UseMagneticField = True']) == {'Verbosity': 2, 'firstRun': 0, 'maxEvents': 100, 'UseMagneticField': True}

def test_case_3():
    assert parse_simulation_config(['maxEvents = 50', 'Verbosity = 3', 'firstRun = 3', 'UseMagneticField = False']) == {'Verbosity': 3, 'firstRun': 3, 'maxEvents': 50, 'UseMagneticField': False}

def test_case_4():
    assert parse_simulation_config(['Verbosity = 4', 'UseMagneticField = True', 'firstRun = 10', 'maxEvents = 20']) == {'Verbosity': 4, 'firstRun': 10, 'maxEvents': 20, 'UseMagneticField': True}

def test_case_5():
    assert parse_simulation_config(['UseMagneticField = True', 'maxEvents = 0', 'Verbosity = 5', 'firstRun = 100']) == {'Verbosity': 5, 'firstRun': 100, 'maxEvents': 0, 'UseMagneticField': True}

def test_case_6():
    assert parse_simulation_config(['firstRun = 5', 'Verbosity = 6', 'UseMagneticField = False', 'maxEvents = 30']) == {'Verbosity': 6, 'firstRun': 5, 'maxEvents': 30, 'UseMagneticField': False}

def test_case_7():
    assert parse_simulation_config(['maxEvents = 1', 'Verbosity = 0', 'UseMagneticField = True', 'firstRun = 7']) == {'Verbosity': 0, 'firstRun': 7, 'maxEvents': 1, 'UseMagneticField': True}

def test_case_8():
    assert parse_simulation_config(['maxEvents = 12', 'firstRun = 8', 'Verbosity = 2', 'UseMagneticField = False']) == {'Verbosity': 2, 'firstRun': 8, 'maxEvents': 12, 'UseMagneticField': False}

def test_case_9():
    assert parse_simulation_config(['UseMagneticField = True', 'firstRun = 9', 'maxEvents = 15', 'Verbosity = 3']) == {'Verbosity': 3, 'firstRun': 9, 'maxEvents': 15, 'UseMagneticField': True}

def test_case_10():
    assert parse_simulation_config(['firstRun = 11', 'maxEvents = 25', 'Verbosity = 4', 'UseMagneticField = False']) == {'Verbosity': 4, 'firstRun': 11, 'maxEvents': 25, 'UseMagneticField': False}

def test_case_11():
    assert parse_simulation_config(['Verbosity = 7', 'UseMagneticField = True', 'firstRun = 12', 'maxEvents = 1000']) == {'Verbosity': 7, 'firstRun': 12, 'maxEvents': 1000, 'UseMagneticField': True}

def test_case_12():
    assert parse_simulation_config(['maxEvents = 200', 'firstRun = 13', 'Verbosity = 8', 'UseMagneticField = False']) == {'Verbosity': 8, 'firstRun': 13, 'maxEvents': 200, 'UseMagneticField': False}

def test_case_13():
    assert parse_simulation_config(['firstRun = 14', 'Verbosity = 9', 'UseMagneticField = True', 'maxEvents = 35']) == {'Verbosity': 9, 'firstRun': 14, 'maxEvents': 35, 'UseMagneticField': True}

def test_case_14():
    assert parse_simulation_config(['UseMagneticField = False', 'firstRun = 15', 'maxEvents = 100', 'Verbosity = 10']) == {'Verbosity': 10, 'firstRun': 15, 'maxEvents': 100, 'UseMagneticField': False}

def test_case_15():
    assert parse_simulation_config(['maxEvents = 45', 'Verbosity = 11', 'firstRun = 16', 'UseMagneticField = True']) == {'Verbosity': 11, 'firstRun': 16, 'maxEvents': 45, 'UseMagneticField': True}

def test_case_16():
    assert parse_simulation_config(['firstRun = 17', 'maxEvents = 55', 'Verbosity = 12', 'UseMagneticField = False']) == {'Verbosity': 12, 'firstRun': 17, 'maxEvents': 55, 'UseMagneticField': False}