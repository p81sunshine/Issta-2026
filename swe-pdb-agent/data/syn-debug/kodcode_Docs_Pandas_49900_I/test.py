from solution import *

import math

from solution import *

import math

from solution import *

import math

import os
import pandas as pd
import matplotlib.pyplot as plt
import pytest
from io import StringIO
from solution import visualize_health_data

# Sample data for testing
sample_data = """age,weight_kg,height_cm,systolic_bp,diastolic_bp,cholesterol
25,68,175,120,80,180
52,85,160,135,85,200
40,74,168,130,90,195
60,78,172,145,95,205
35,70,180,125,85,190
"""

def test_visualize_health_data(monkeypatch):
    # Creating a mock file from sample data
    test_file_path = "test_data.csv"
    with open(test_file_path, 'w') as f:
        f.write(sample_data)

    try:
        # Running the visualization function
        visualize_health_data(test_file_path)
        
        # Check that plots are generated (no assertion errors thrown means success for this task)
        assert True
    finally:
        # Clean up the test file
        if os.path.exists(test_file_path):
            os.remove(test_file_path)