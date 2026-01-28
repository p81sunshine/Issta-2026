from solution import *

import math

from solution import *

import math

from solution import *

import math

import pandas as pd
from solution import load_data, plot_runtime_vs_rating, plot_runtime_vs_rating_with_genre, plot_custom_runtime_vs_rating, plot_votes_over_years, plot_facet_runtime_vs_rating

def test_load_data():
    # Create a sample dataframe for testing
    sample_data = {
        'Title': ['Movie1', 'Movie2'],
        'Genre': ['Action', 'Comedy'],
        'Director': ['Director1', 'Director2'],
        'Year': [2000, 2001],
        'Runtime': [120, 90],
        'Rating': [8.0, 7.5],
        'Votes': [200000, 150000]
    }
    df = pd.DataFrame(sample_data)
    df.to_csv('test_movies.csv', index=False)
    
    # Testing the load_data function
    loaded_df = load_data('test_movies.csv')
    assert loaded_df.equals(df)

def test_plot_runtime_vs_rating():
    sample_data = {
        'Title': ['Movie1', 'Movie2'],
        'Genre': ['Action', 'Comedy'],
        'Director': ['Director1', 'Director2'],
        'Year': [2000, 2001],
        'Runtime': [120, 90],
        'Rating': [8.0, 7.5],
        'Votes': [200000, 150000]
    }
    df = pd.DataFrame(sample_data)
    plot_runtime_vs_rating(df)

def test_plot_runtime_vs_rating_with_genre():
    sample_data = {
        'Title': ['Movie1', 'Movie2'],
        'Genre': ['Action', 'Comedy'],
        'Director': ['Director1', 'Director2'],
        'Year': [2000, 2001],
        'Runtime': [120, 90],
        'Rating': [8.0, 7.5],
        'Votes': [200000, 150000]
    }
    df = pd.DataFrame(sample_data)
    plot_runtime_vs_rating_with_genre(df)

def test_plot_custom_runtime_vs_rating():
    sample_data = {
        'Title': ['Movie1', 'Movie2'],
        'Genre': ['Action', 'Comedy'],
        'Director': ['Director1', 'Director2'],
        'Year': [2000, 2001],
        'Runtime': [120, 90],
        'Rating': [8.0, 7.5],
        'Votes': [200000, 150000]
    }
    df = pd.DataFrame(sample_data)
    plot_custom_runtime_vs_rating(df)

def test_plot_votes_over_years():
    sample_data = {
        'Title': ['Movie1', 'Movie2'],
        'Genre': ['Action', 'Comedy'],
        'Director': ['Director1', 'Director2'],
        'Year': [2000, 2001],
        'Runtime': [120, 90],
        'Rating': [8.0, 7.5],
        'Votes': [200000, 150000]
    }
    df = pd.DataFrame(sample_data)
    plot_votes_over_years(df)

def test_plot_facet_runtime_vs_rating():
    sample_data = {
        'Title': ['Movie1', 'Movie2', 'Movie3', 'Movie4'],
        'Genre': ['Action', 'Comedy', 'Action', 'Comedy'],
        'Director': ['Director1', 'Director2', 'Director3', 'Director4'],
        'Year': [2000, 2001, 2002, 2003],
        'Runtime': [120, 90, 110, 95],
        'Rating': [8.0, 7.5, 7.0, 9.0],
        'Votes': [200000, 150000, 120000, 180000]
    }
    df = pd.DataFrame(sample_data)
    plot_facet_runtime_vs_rating(df)