import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix

def visualize_health_data(file_path):
    # Read the dataset
    data = pd.read_csv(file_path)
    
    # Task 1: Visualize Blood Pressure Trends
    
    # Scatter plot of age vs systolic_bp
    plt.figure(figsize=(10, 6))
    plt.scatter(data['age'], data['conda_bp'])
    plt.xlabel('Age')
    plt.ylabel('Systolic Blood Pressure')
    plt.title('Age vs Systolic Blood Pressure')
    plt.grid(True)
    plt.show()
    
    # Line plot of age vs difference between systolic_bp and diastolic_bp
    bp_diff = data['systolic_bp'] - data['diastolic_bp']
    plt.figure(figsize=(10, 6))
    plt.plot(data['age'], bp_diff, marker='o')
    plt.xlabel('Age')
    plt.ylabel('Difference (Systolic BP - Diastolic BP)')
    plt.title('Age vs Blood Pressure Difference')
    plt.grid(True)
    plt.show()
    
    # Task 2: Analyze Cholesterol Levels
    
    # Preparing age groups for boxplot
    bins = [20, 30, 40, 50, 60, 70]
    labels = ['20-30', '31-40', '41-50', '51-60', '61-70']
    data['age_group'] = pd.cut(data['age'], bins=bins, labels=labels, right=False)
    
    # Boxplot for cholesterol levels by age group
    plt.figure(figsize=(10, 6))
    data.boxplot(column='cholesterol', by='age_group')
    plt.xlabel('Age Group')
    plt.ylabel('Cholesterol Level')
    plt.title('Cholesterol Levels by Age Group')
    plt.suptitle('')
    plt.grid(True)
    plt.show()
    
    # Task 3: Weight and Height Distribution
    
    # Scatter matrix for age, weight_kg, height_cm, and cholesterol
    plt.figure(figsize=(12, 8))
    scatter_matrix(data[['age', 'weight_kg', 'height_cm', 'cholesterol']], diagonal='kde')
    plt.suptitle('Scatter Matrix of Age, Weight, Height, and Cholesterol')
    plt.show()