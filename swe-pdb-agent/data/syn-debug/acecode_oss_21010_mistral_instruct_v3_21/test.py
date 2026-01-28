import pytest
from acecode_oss_21010_mistral_instruct_v3_21_code import simple_login_system, __init__

def test_case_0():
    assert simple_login_system([('register', 'user1', 'pass1', 'user1@example.com')]) == ['User registered successfully']

def test_case_1():
    assert simple_login_system([('register', 'user1', 'pass1', 'user1@example.com'), ('register', 'user1', 'pass2', 'user1@another.com')]) == ['User registered successfully', 'Error: Username already taken']

def test_case_2():
    assert simple_login_system([('register', 'user1', 'pass1', 'user1@example.com'), ('authenticate', 'user1', 'pass1')]) == ['User registered successfully', 'User authenticated successfully']

def test_case_3():
    assert simple_login_system([('register', 'user2', 'pass2', 'user2@example.com'), ('authenticate', 'user2', 'wrongpass')]) == ['User registered successfully', 'Error: Invalid username or password']

def test_case_4():
    assert simple_login_system([('register', 'user3', 'pass3', 'user3@example.com'), ('get_info', 'user3')]) == ['User registered successfully', 'Username: user3, Email: user3@example.com']

def test_case_5():
    assert simple_login_system([('get_info', 'user4')]) == ['Error: User not found']

def test_case_6():
    assert simple_login_system([('register', 'user5', 'pass5', 'user5@example.com'), ('register', 'user6', 'pass6', 'user6@example.com'), ('authenticate', 'user6', 'pass6')]) == ['User registered successfully', 'User registered successfully', 'User authenticated successfully']

def test_case_7():
    assert simple_login_system([('register', 'user7', 'pass7', 'user7@example.com'), ('get_info', 'user7')]) == ['User registered successfully', 'Username: user7, Email: user7@example.com']

def test_case_8():
    assert simple_login_system([('register', 'user8', 'pass8', 'user8@example.com'), ('authenticate', 'user8', 'pass9')]) == ['User registered successfully', 'Error: Invalid username or password']

def test_case_9():
    assert simple_login_system([('register', 'user9', 'pass9', 'user9@example.com'), ('get_info', 'user10')]) == ['User registered successfully', 'Error: User not found']

def test_case_10():
    assert simple_login_system([('register', 'admin', 'adminpass', 'admin@example.com'), ('get_info', 'admin')]) == ['User registered successfully', 'Username: admin, Email: admin@example.com']

def test_case_11():
    assert simple_login_system([('register', 'user11', 'pass11', 'user11@example.com'), ('authenticate', 'user11', 'pass11')]) == ['User registered successfully', 'User authenticated successfully']

def test_case_12():
    assert simple_login_system([('register', 'user12', 'pass12', 'user12@example.com'), ('get_info', 'user12')]) == ['User registered successfully', 'Username: user12, Email: user12@example.com']

def test_case_13():
    assert simple_login_system([('register', 'user13', 'pass13', 'user13@example.com'), ('register', 'user13', 'pass14', 'user13@another.com'), ('get_info', 'user13')]) == ['User registered successfully', 'Error: Username already taken', 'Username: user13, Email: user13@example.com']

def test_case_14():
    assert simple_login_system([('authenticate', 'nonexistent', 'pass')]) == ['Error: Invalid username or password']

def test_case_15():
    assert simple_login_system([('register', 'user14', 'pass14', 'user14@example.com'), ('authenticate', 'user14', 'pass14'), ('get_info', 'user14')]) == ['User registered successfully', 'User authenticated successfully', 'Username: user14, Email: user14@example.com']

def test_case_16():
    assert simple_login_system([('authenticate', 'user15', 'pass15'), ('get_info', 'user15')]) == ['Error: Invalid username or password', 'Error: User not found']

def test_case_17():
    assert simple_login_system([('register', 'user16', 'pass16', 'user16@example.com'), ('get_info', 'user16')]) == ['User registered successfully', 'Username: user16, Email: user16@example.com']