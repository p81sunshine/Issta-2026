import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
    """Load the data from a CSV file."""
    return pd.read_csv(file_path, index_col=0)


def plot_runtime_vs_rating(movies):
    """Basic scatter plot: Runtime vs. Rating."""
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=movies, x='Runtime', y='Rating')
    plt.title('Runtime vs. Rating')
    plt.xlabel('Runtime (minutes)')
    plt.ylabel('Rating')
    plt.show()


def plot_runtime_vs_rating_with_genre(movies):
    """Scatter plot with hue: Runtime vs. Rating by Genre."""
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=movies, x='Runtime', y='Rating', hue='Genre')
    plt.title('Runtime vs. Rating by Genre')
    plt.xlabel('Runtime (minutes)')
    plt.ylabel('Rating')
    plt.legend(title='Genre')
    plt.show()


def plot_custom_runtime_vs_rating(movies):
    """Custom scatter plot: Runtime vs. Rating by Genre with Marker Style."""
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=movies, x='Runtime', y='Rating', hue='Genre', style=movies['Rating'] > 7.5)
    plt.title('Runtime vs. Rating by Genre with Marker Style')
    plt.xlabel('Runtime (minutes)')
    plt.ylabel('Rating')
    plt.legend(title='Genre')
    plt.show()


def plot_votes_over_years(movies):
    """Line plot: Votes over the Years."""
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=movies, x='Year', y='Votes', errorbar='sd')
    plt.title('Votes over the Years')
    plt.xlabel('Year')
    plt.ylabel('Votes')
    plt.show()


def plot_facet_runtime_vs_rating(movies):
    """Faceted scatter plot: Runtime vs. Rating by Genre."""
    g = sns.FacetGrid(movies, col='Genre', col_wrap=4, height=4)
    g.map(sns.scatterplot, 'Runtime', 'Rating')
    g.add_legend()
    plt.show()