from solution import *
import math

def test_all():
    try:
        import pandas as pd
        import numpy as np
    except:
        # fine
        pass

    house_data = {
        'Location': ['Location 1', 'Location 2', 'Location 3', 'Location 4', 'Location 5',
                     'Location 6', 'Location 7', 'Location 8', 'Location 9', 'Location 10'],
        'Bedrooms': [3.0, 4.0, 2.0, 5.0, 3.0, 4.0, 2.0, 3.0, 4.0, 3.0],
        'Bathrooms': [2.5, 3.0, 1.0, 4.0, 2.0, 3.5, 1.5, 2.0, 3.0, 2.0],
        'Area': [2000.0, 2500.0, 1500.0, 3500.0, 1800.0, 2800.0, 1200.0, 2100.0, 2200.0, 1900.0],
        'Price': [350000.0, 500000.0, 250000.0, 700000.0, 400000.0, 600000.0, 300000.0, 450000.0, 480000.0, 420000.0],
        "Sold": [0, 0, 1, 0, 1, 1, 0, 1, 0, 1]
    }

    house_df = pd.DataFrame(house_data)
    X1 = house_df[['Bedrooms', 'Bathrooms', 'Area', 'Price']]
    y1 = house_df['Sold']
    model1 = regression(X1, y1)

    assert np.allclose(
        model1.coef_, [-0.11855473, -0.16288398, -0.02635437, 0.00332171])
    assert np.isclose(model1.alpha_, 2.00)
    assert np.isclose(model1.intercept_, 0.6395470662223749)

    coffee_data = {
        'Location': ['Coffee Shop 1', 'Coffee Shop 2', 'Coffee Shop 3', 'Coffee Shop 4', 'Coffee Shop 5',
                     'Coffee Shop 6', 'Coffee Shop 7', 'Coffee Shop 8', 'Coffee Shop 9', 'Coffee Shop 10'],
        'Quality': [4.2, 4.5, 4.0, 4.8, 4.3, 4.6, 4.1, 4.4, 4.7, 4.2],
        'Price': [8.5, 9.0, 8.0, 10.0, 8.7, 9.5, 8.2, 9.3, 9.8, 8.6],
        'Revenue': [850.0, 1080.0, 640.0, 1500.5, 957.0, 1235.0, 738.0, 976.5, 1225.5, 817.0],
        'Available': [1, 1, 0, 1, 0, 1, 0, 1, 1, 0]
    }

    coffee_df = pd.DataFrame(coffee_data)
    X2 = coffee_df[['Quality', 'Price', 'Revenue']]
    y2 = coffee_df['Available']
    model2 = regression(X2, y2)

    assert np.allclose(
        model2.coef_, [0.3113473924714517, 0.32343973993669595, 0.23378643236198743])
    assert np.isclose(model2.alpha_, 1)
    assert np.isclose(model2.intercept_, 0.19852190097946043)