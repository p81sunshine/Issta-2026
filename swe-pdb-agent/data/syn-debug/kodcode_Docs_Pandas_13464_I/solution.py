import pandas as pd
import matplotlib.pyplot as plt

def load_dataset(file_path: str) -> pd.DataFrame:
    """
    Load the dataset from a CSV file into a pandas DataFrame.
    
    Args:
    - file_path (str): Path to the CSV file containing the dataset.
    
    Returns:
    - pd.DataFrame: Loaded DataFrame.
    """
    return pd.read_csv(file_path, on_bad_lines='skip')


def explore_dataset(df: pd.DataFrame):
    """
    Perform initial exploration of the dataset.
    
    Args:
    - df (pd.DataFrame): DataFrame to explore.
    
    Prints:
    - First few rows of the DataFrame.
    - Summary of the dataset.
    """
    print("First few records:")
    print(df.head())
    print("\nSummary of the dataset:")
    print(df.info())
    print(df.describe())


def clean_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean the dataset by handling missing values and standardizing the genre column.
    
    Args:
    - df (pd.DataFrame): DataFrame to clean.
    
    Returns:
    - pd.DataFrame: Cleaned DataFrame.
    """
    # Remove rows where the rating and revenue are missing
    df = df.dropna(subset=['rating', 'revenue'])

    # Standardize the genre column to lowercase
    df['genre'] = df['genre'].str.lower()

    return df


def average_rating_by_genre(df: pd.DataFrame) -> pd.Series:
    """
    Compute the average rating for each genre.
    
    Args:
    - df (pd.DataFrame): DataFrame containing movie data.
    
    Returns:
    - pd.Series: Average rating for each genre.
    """
    return df.groupby('genre')['rating'].mean()


def top_5_highest_grossing(df: pd.DataFrame) -> pd.DataFrame:
    """
    Get the top 5 highest-grossing movies.
    
    Args:
    - df (pd.DataFrame): DataFrame containing movie data.
    
    Returns:
    - pd.DataFrame: DataFrame of top 5 highest-grossing movies.
    """
    return df.nlargest(5, 'revenue')


def visualize_revenue_distribution(df: pd.DataFrame):
    """
    Visualize the distribution of movie revenues using a histogram.
    
    Args:
    - df (pd.DataFrame): DataFrame containing movie data.
    
    Creates:
    - Histogram of movie revenues.
    """
    plt.hist(df['revenue'], bins=30, edgecolor='k')
    plt.xlabel('Revenue (in millions)')
    plt.ylabel('Frequency')
    plt.title('Distribution of Movie Revenues')
    plt.show()


def export_dataset(df: pd.DataFrame, file_path: str):
    """
    Export the DataFrame to a CSV file.
    
    Args:
    - df (pd.DataFrame): DataFrame to export.
    - file_path (str): Path to save the new CSV file.
    
    Exports the DataFrame to a CSV file.
    """
    df.to_csv(file_path, index=True)