from solution import *

import math

from solution import *

import math

from solution import *

import math

import pandas as pd
from io import StringIO
import pytest

from solution import (load_dataset, explore_dataset, clean_dataset,
                      average_rating_by_genre, top_5_highest_grossing,
                      visualize_revenue_distribution, export_dataset)

# Sample test data
csv_data = """
title,genre,year,rating,revenue
Inception,Sci-Fi,2010,8.8,829.89
The Dark Knight,Action,2008,9.0,1004.45
Interstellar,Sci-Fi,2014,8.6,677.47
Prestige,Drama,2006,8.5,109.46
Batman Begins,Action,2005,8.2,373.71
"""

def test_load_dataset():
    df = load_dataset(StringIO(csv_data))
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (5, 5)

def test_explore_dataset():
    df = load_dataset(StringIO(csv_data))
    explore_dataset(df)  # Visual check, no assert needed

def test_clean_dataset():
    df = load_dataset(StringIO(csv_data))
    df.loc[0, 'rating'] = None  # Introduce a missing value for testing
    df_clean = clean_dataset(df)
    assert df_clean.shape == (4, 5)  # One row should be removed

def test_average_rating_by_genre():
    df = load_dataset(StringIO(csv_data))
    df = clean_dataset(df)
    avg_rating = average_rating_by_genre(df)
    assert avg_rating['sci-fi'] == pytest.approx((8.8 + 8.6) / 2)
    assert avg_rating['action'] == pytest.approx((9.0 + 8.2) / 2)
    assert avg_rating['drama'] == 8.5

def test_top_5_highest_grossing():
    df = load_dataset(StringIO(csv_data))
    df = clean_dataset(df)
    top_5 = top_5_highest_grossing(df)
    assert top_5.shape == (5, 5)
    assert top_5.iloc[0]['title'] == 'The Dark Knight'

def test_visualize_revenue_distribution():
    df = load_dataset(StringIO(csv_data))
    df = clean_dataset(df)
    visualize_revenue_distribution(df)  # Visual check, no assert needed

def test_export_dataset(tmp_path):
    df = load_dataset(StringIO(csv_data))
    df = clean_dataset(df)
    temp_file = tmp_path / "cleaned_movies.csv"
    export_dataset(df, temp_file)
    assert temp_file.exists()
    df_exported = pd.read_csv(temp_file)
    assert df_exported.shape == df.shape
    assert list(df_exported.columns) == list(df.columns)