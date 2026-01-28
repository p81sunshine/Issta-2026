from solution import *

import math

from solution import *

import math

from solution import *

import math

import pytest
import pandas as pd
from io import StringIO

from solution import display_first_10_rows, add_column_and_save, drop_column_and_save

def test_display_first_10_rows(capsys):
    # Create a mock CSV data
    data = """col1,col2
1,2
3,4
5,6
7,8
9,10
11,12
13,14
15,16
17,18
19,20
21,22"""
    # Create a StringIO object to simulate a file
    mock_csv = StringIO(data)
    # Load dataframe to file-like object
    df = pd.read_csv(mock_csv)
    # Save to temporary csv
    df.to_csv('test_display.csv', index=False)
    
    # Call the function
    display_first_10_rows('test_display.csv')
    
    # Capture the output
    captured = capsys.readouterr()
    
    # Check that the output contains the expected result
    expected_output = """   col1  col2
0     1     2
1     3     4
2     5     6
3     7     8
4     9    10
5    11    12
6    13    14
7    15    16
8    17    18
9    19    20
"""
    assert captured.out == expected_output

def test_add_column_and_save():
    # Create a mock CSV data
    data = """col1,col2
1,2
3,4
5,6"""
    # Create a StringIO object to simulate a file
    mock_csv = StringIO(data)
    # Load dataframe to file-like object
    df = pd.read_csv(mock_csv)
    # Save to temporary csv
    df.to_csv('test_add_column.csv', index=False)
    
    # Call the function
    add_column_and_save('test_add_column.csv')
    
    # Verify the new file content
    df_modified = pd.read_csv('modified_data.csv')
    assert 'status' in df_modified.columns
    assert (df_modified['status'] == 'active').all()

def test_drop_column_and_save():
    # Create a mock modified CSV data with status column
    data = """col1,col2,status
1,2,active
3,4,active
5,6,active"""
    # Create a StringIO object to simulate a file
    mock_csv = StringIO(data)
    # Load dataframe to file-like object
    df = pd.read_csv(mock_csv)
    # Save to temporary csv
    df.to_csv('test_drop_column.csv', index=False)
    
    # Call the function
    drop_column_and_save('test_drop_column.csv')
    
    # Verify the new file content
    df_modified = pd.read_csv('modified_data_without_status.csv')
    assert 'status' not in df_modified.columns