from solution import *

import math

from solution import *

import math

from solution import *

import math

from solution import combine_sales_data, merge_with_inventory, update_and_compare_sales, asof_merge_sales_quotes

def test_combine_sales_data():
    branch_a = pd.DataFrame({
        'Product': ['A', 'B', 'C'],
        'Date': ['2023-01-01', '2023-01-02', '2023-01-03'],
        'Quantity': [10, 20, 15],
        'Amount': [100, 200, 150]
    })

    branch_b = pd.DataFrame({
        'Product': ['A', 'B', 'D'],
        'Date': ['2023-01-01', '2023-01-04', '2023-01-05'],
        'Quantity': [8, 18, 5],
        'Amount': [80, 180, 50]
    })

    result = combine_sales_data(branch_a, branch_b)
    assert len(result) == 6
    assert list(result['Product']) == ['A', 'B', 'C', 'A', 'B', 'D']

def test_merge_with_inventory():
    combined_sales = combine_sales_data(branch_a_sales, branch_b_sales)
    result = merge_with_inventory(combined_sales, inventory)
    
    assert 'Stock' in result.columns
    assert result.loc[result['Product'] == 'A', 'Stock'].values[0] == 50
    assert result.loc[result['Product'] == 'D', 'Stock'].values[0] == 80

def test_update_and_compare_sales():
    combined_sales = combine_sales_data(branch_a_sales, branch_b_sales)
    updated_sales, differences = update_and_compare_sales(combined_sales)
    
    assert updated_sales.loc[0, 'Quantity'] == 12
    assert updated_sales.loc[0, 'Amount'] == 120
    assert updated_sales.loc[4, 'Quantity'] == 19
    assert updated_sales.loc[4, 'Amount'] == 190

    assert not differences.empty
    assert differences.shape[0] == 2

def test_asof_merge_sales_quotes():
    sales_data = pd.DataFrame({
        'Product': ['A', 'B', 'A', 'D'],
        'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-05'],
        'Quantity': [10, 20, 15, 5],
        'Amount': [100, 200, 150, 50]
    })

    quotes_data = pd.DataFrame({
        'Product': ['A', 'B', 'B', 'D'],
        'Date': ['2023-01-01', '2023-01-03', '2023-01-05', '2023-01-06'],
        'Quote': [95, 185, 190, 45]
    })

    result = asof_merge_sales_quotes(sales_data, quotes_data)
    
    assert not result.empty
    assert 'Quote' in result.columns
    assert result.loc[result['Product'] == 'A', 'Quote'].values[0] == 95
    assert result.loc[result['Product'] == 'B', 'Quote'].values[1] == 190