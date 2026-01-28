from solution import *

import math

from solution import *

import math

from solution import *

import math

from solution import execute_operations

def test_insert_and_inorder():
    operations = [
        "Insert 10",
        "Inorder"
    ]
    assert execute_operations(operations) == ["10"]

def test_insert_delete_inorder():
    operations = [
        "Insert 10",
        "Insert 5",
        "Insert 15",
        "Delete 10",
        "Inorder"
    ]
    assert execute_operations(operations) == ["5 15"]

def test_search():
    operations = [
        "Insert 10",
        "Insert 5",
        "Search 5",
        "Search 15"
    ]
    assert execute_operations(operations) == ["Yes", "No"]

def test_min_max():
    operations = [
        "Insert 10",
        "Insert 5",
        "Insert 15",
        "Min",
        "Max"
    ]
    assert execute_operations(operations) == ["5", "15"]

def test_empty_operations():
    operations = [
        "Min", 
        "Max", 
        "Inorder"
    ]
    assert execute_operations(operations) == ["Empty", "Empty", "Empty"]

def test_mixed_operations():
    operations = [
        "Insert 10",
        "Insert 20",
        "Insert 5",
        "Delete 10",
        "Min",
        "Max",
        "Search 20",
        "Inorder"
    ]
    assert execute_operations(operations) == ["5", "20", "Yes", "5 20"]