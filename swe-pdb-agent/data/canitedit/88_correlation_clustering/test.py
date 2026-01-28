from solution import *
import math

import numpy as np
import pandas as pd
from scipy.cluster.hierarchy import linkage, fcluster
from scipy.spatial.distance import squareform

def test_all():
    house_data = {
        'Location': ['Location 1', 'Location 2', 'Location 3', 'Location 4', 'Location 5',
                    'Location 6', 'Location 7', 'Location 8', 'Location 9', 'Location 10'],
        'Bedrooms': [3.0, 4.0, 2.0, 5.0, 3.0, 4.0, 2.0, 3.0, 4.0, 3.0],
        'Bathrooms': [2.5, 3.0, 1.0, 4.0, 2.0, 3.5, 1.5, 2.0, 3.0, 2.0],
        'Area': [764, 893, 215, 417, 110, 545, 690, 812, 793, 313],
        'Price': [574026, 726031, 854329, 860920, 301285, 926927, 229785, 706875, 134550, 572562],
        "Sold": [0, 0, 1, 0, 1, 1, 0, 1, 0, 1]
    }
    
    feat = FeatureSelector(pd.DataFrame(house_data), ["Bedrooms", "Bathrooms", "Area", "Price"])
    corr_matrix = [[1.0, 0.9670962107805764, 0.20910102028026062, 0.27480987061476353], [0.9670962107805764, 1.0, 0.28631105178011296, 0.2738329357250021], [0.20910102028026062, 0.28631105178011296, 1.0, -0.11753185550442], [0.27480987061476353, 0.2738329357250021, -0.11753185550442, 1.0]]
    assert np.allclose(feat.corr_matrix().values, corr_matrix)
    assert feat.cluster(0.6) == [['Bedrooms', 'Bathrooms'], ['Area'], ['Price']]
    assert feat.cluster(0.95) == [['Bedrooms', 'Bathrooms', 'Area', 'Price']]
    assert feat.cluster(0) == [['Bedrooms'], ['Bathrooms'], ['Area'], ['Price']]
    assert feat.select_features(feat.cluster(0.6)) == ["Bedrooms", "Area", "Price"]
    assert feat.select_features(feat.cluster(0.95)) == ["Bedrooms"]
    assert feat.select_features(feat.cluster(0)) == ['Bedrooms', 'Bathrooms', 'Area', 'Price']
    
    coffee_data = {
        'Location': ['Cafe 1', 'Cafe 2', 'Cafe 3', 'Cafe 4', 'Cafe 5',
                    'Cafe 6', 'Cafe 7', 'Cafe 8', 'Cafe 9', 'Cafe 10'],
        'Seats': [20, 35, 50, 30, 15, 40, 55, 25, 10, 45],
        'Parking': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'Area': [764, 893, 215, 417, 110, 545, 690, 812, 793, 313],
        'Rating': [4.5, 4.2, 4.7, 4.0, 4.3, 4.8, 4.5, 4.1, 4.6, 4.4],
        'Sold Coffee': [150, 200, 300, 180, 120, 250, 350, 160, 90, 220],
        'Revenue': [3000, 4500, 6000, 4200, 2400, 5500, 7500, 3200, 1800, 4800],
        "Sold": [0, 0, 1, 0, 1, 1, 0, 1, 0, 1],
    }
    
    feat = FeatureSelector(pd.DataFrame(coffee_data), ["Seats", "Parking", "Area", "Rating", "Sold Coffee", "Revenue"])
    corr_matrix = [[1.0, np.nan, -0.1836777096084065, 0.2609973560091334, 0.9661648759246296, 0.9708232777362824], [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan], [-0.1836777096084065, np.nan, 1.0, -0.10646001129209194, -0.13774106670179073, -0.11483948421273826], [0.2609973560091334, np.nan, -0.10646001129209194, 1.0, 0.34902746718144245, 0.2927869919933592], [0.9661648759246296, np.nan, -0.13774106670179073, 0.34902746718144245, 1.0, 0.9908535188301559], [0.9708232777362824, np.nan, -0.11483948421273826, 0.2927869919933592, 0.9908535188301559, 1.0]]
    assert np.allclose(feat.corr_matrix().values, corr_matrix, equal_nan=True)
    assert feat.cluster(0.6) == [['Seats', 'Sold Coffee', 'Revenue'], ['Parking'], ['Area'], ['Rating']]
    assert feat.cluster(0) == [['Seats'], ['Parking'], ['Area'], ['Rating'], ['Sold Coffee'], ['Revenue']]
    assert feat.cluster(0.3) == [['Seats', 'Sold Coffee', 'Revenue'], ['Parking'], ['Area'], ['Rating']]
    assert feat.cluster(0.8) == [['Seats', 'Rating', 'Sold Coffee', 'Revenue'], ['Parking'], ['Area']]
    assert feat.cluster(1) == [['Seats', 'Parking', 'Area', 'Rating', 'Sold Coffee', 'Revenue']]
    assert feat.select_features(feat.cluster(0.6)) == ["Seats", "Parking", "Area", "Rating"]
    assert feat.select_features(feat.cluster(0)) == ["Seats", "Parking", "Area", "Rating", "Sold Coffee", "Revenue"]
    assert feat.select_features(feat.cluster(0.3)) ==  ["Seats", "Parking", "Area", "Rating"]
    assert feat.select_features(feat.cluster(0.8)) == ["Seats", "Parking", "Area"]
    assert feat.select_features(feat.cluster(1.0)) ==  ["Seats"]