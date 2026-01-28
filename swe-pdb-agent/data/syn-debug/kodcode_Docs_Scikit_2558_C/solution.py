import pandas as pd
from sklearn.impute import SimpleImputer, KNNImputer
from sklearn.experimental import enable_iterative_imputer  # noqa
from sklearn.impute import IterativeImputer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

def impute_and_evaluate(imputer_method: str, data_file: str) -> float:
    """
    Impute missing values in the dataset and evaluate a DecisionTreeClassifier.

    Args:
    imputer_method (str): The imputation method to use ('simple', 'iterative', or 'knn').
    data_file (str): Path to the dataset CSV file.

    Returns:
    float: The accuracy score of the trained model on the test set.
    """
    # Load dataset
    data = pd.read_csv(data_file)
    
    # Extract features and target
    features = data.drop(columns=['Target'])
    target = data['Target']
    
    # Encode categorical features
    label_encoders = {}
    for column in features.select_dtypes(include=['object']).columns:
        le = LabelEncoder()
        features[column] = le.fit_transform(features[column].astype(str))
        label_encoders[column] = le

    if imputer_method == 'simple':
        # Simple Imputer
        imputer_num = SimpleImputer(strategy='mean')
        imputer_cat = SimpleImputer(strategy='most_frequent')
        features[['Feature1', 'Feature2']] = imputer_num.fit_transform(features[['Feature1', 'Feature2']])
        features['Feature3'] = imputer_cat.fit_transform(features['Feature3'])
        
    elif imputer_method == 'iterative':
        # Iterative Imputer
        imputer = IterativeImputer()
        features[['Feature1', 'Feature2', 'Feature3']] = imputer.fit_transform(features[['Feature1', 'Feature2', 'Feature3']])
        
    elif imputer_method == 'knn':
        # KNN Imputer
        imputer = KNNImputer()
        features = imputer.fit_transform(features)
        features = pd.DataFrame(features, columns=data.columns[:-1])
    else:
        raise ValueError(f"Unknown imputer method: {imputer_method}")

    # Split dataset into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)
    
    # Train and evaluate model
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    return accuracy