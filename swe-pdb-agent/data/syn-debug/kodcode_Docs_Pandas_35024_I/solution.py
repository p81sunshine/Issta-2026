import pandas as pd

# Create dataframes
branch_a_sales = pd.DataFrame({
    'Product': ['A', 'B', 'C'],
    'Date': ['2023-01-01', '2023-01-02', '2023-01-03'],
    'Quantity': [10, 20, 15],
    'Amount': [100, 200, 150]
})

branch_b_sales = pd.DataFrame({
    'Product': ['A', 'B', 'D'],
    'Date': ['2023-01-01', '2023-01-04', '2023-01-05'],
    'Quantity': [8, 18, 5],
    'Amount': [80, 180, 50]
})

inventory = pd.DataFrame({
    'Product': ['A', 'B', 'C', 'D'],
    'Stock': [50, 60, 70, 80]
})

# Task 1: Combine DataFrames
def combine_sales_data(df1, df2):
    combined_df = pd.concat([df1, df2], ignore_index=True)
    combined_df = combined_df.reset_index(drop=True)
    combined_df = combined_df.drop_duplicates()
    return combined_df

# Task 2: Merge with Inventory
def merge_with_inventory(sales_df, inventory_df):
    merged_df = pd.merge(sales_df, inventory_df, on='Product', how='inner')
    return merged_df

# Task 3: Data Update and Comparison
def update_and_compare_sales(sales_df):
    updated_sales_df = sales_df.copy()

    updated_sales_df.loc[0, 'Quantity'] = 12
    updated_sales_df.loc[0, 'Amount'] = 120
    updated_sales_df.loc[4, 'Quantity'] = 19
    updated_sales_df.loc[4, 'Amount'] = 190

    differences = updated_sales_df.compare(updated_sales_df)

    return updated_sales_df, differences

# Task 4: Advanced Task - asof merge
def asof_merge_sales_quotes(sales_df, quotes_df):
    sales_df['Date'] = pd.to_datetime(sales_df['Date'])
    quotes_df['Date'] = pd.to_datetime(quotes_df['Date'])

    merged_df = pd.merge_asof(sales_df.sort_values('Date'),
                              quotes_df.sort_values('Date'),
                              on='Date',
                              by='Product',
                              direction='backward')

    return merged_df