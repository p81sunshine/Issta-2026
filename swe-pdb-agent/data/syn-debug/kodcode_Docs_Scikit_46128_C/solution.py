from sklearn.datasets import load_iris
from sklearn.feature_selection import VarianceThreshold, SelectKBest, f_classif, RFE, SelectFromModel
from sklearn.ensemble import ExtraTreesClassifier, RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def get_accuracies():
    """Use different feature selection methods provided by the `sklearn.feature_selection` 
    module to pre-process the Iris dataset and compare their impacts on a Random Forest 
    classification model's performance.

    >>> accuracies = get_accuracies()
    >>> "No Feature Selection" in accuracies
    True
    >>> "Variance Threshold" in accuracies
    True
    >>> "SelectKBest" in accuracies
    True
    >>> "RFE" in accuracies
    True
    >>> "Tree-based" in accuracies
    True
    """
    # Load Iris dataset
    X, y = load_iris(return_X_y=True)

    # Split the dataset
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    def evaluate_model(X_train, X_test, y_train, y_test):
        clf = RandomForestClassifier(random_state=42)
        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)
        return accuracy_score(y_test, y_pred)

    # 1. No feature selection
    acc_no_selection = evaluate_model(X_train, X_test, y_train, y_test)
    # 2. Variance Threshold
    sel = VarianceThreshold(threshold=0.1)
    X_train_vt = sel.fit_transform(X_train)
    X_test_vt = sel.transform(X_test)
    acc_variance_threshold = evaluate_model(X_train_vt, X_test_vt, y_train, y_test)
    # 3. SelectKBest
    sel = SelectKBest(f_classif, k=2)
    X_train_kbest = sel.fit_transform(X_train, y_train)
    X_test_kbest = sel.transform(X_test)
    acc_select_kbest = evaluate_model(X_train_kbest, X_test_kbest, y_train, y_test)
    # 4. Recursive Feature Elimination (RFE)
    estimator = LogisticRegression(max_iter=1000)
    sel = RFE(estimator, n_features_to_select=2, step=1)
    X_train_rfe = sel.fit_transform(X_train, y_train)
    X_test_rfe = sel.transform(X_test)
    acc_rfe = evaluate_model(X_train_rfe, X_test_rfe, y_train, y_test)
    # 5. Tree-based feature selection
    clf = ExtraTreesClassifier(n_estimators=50, random_state=42)
    clf.fit(X_train, y_train)
    model = SelectFromModel(clf, prefit=True)
    X_train_tree = model.transform(X_train)
    X_test_tree = model.transform(X_test)
    acc_tree = evaluate_model(X_train_tree, X_test_tree, y_train, y_test)

    # Collect the accuracy results
    accuracy_results = {
        "No Feature Selection": acc_no_selection,
        "Variance Threshold": acc_variance_threshold,
        "SelectKBest": acc_select_kbest,
        "RFE": acc_rfe,
        "Tree-based": acc_tree
    }

    return accuracy_results

X, y = load_iris(return_X_y=True)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

def evaluate_model(X_train, X_test, y_train, y_test):
    clf = RandomForestClassifier(random_state=42)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    return accuracy_score(y_test, y_pred)

# 1. No feature selection
acc_no_selection = evaluate_model(X_train, X_test, y_train, y_test)
# 2. Variance Threshold
sel = VarianceThreshold(threshold=0.1)
X_train_vt = sel.fit_transform(X_train)
X_test_vt = sel.transform(X_test)
acc_variance_threshold = evaluate_model(X_train_vt, X_test_vt, y_train, y_test)
# 3. SelectKBest
sel = SelectKBest(f_classif, k=2)
X_train_kbest = sel.fit_transform(X_train, y_train)
X_test_kbest = sel.transform(X_test)
acc_select_kbest = evaluate_model(X_train_kbest, X_test_kbest, y_train, y_test)
# 4. Recursive Feature Elimination (RFE)
estimator = LogisticRegression(max_iter=1000)
sel = RFE(RandomForestClassifier(random_state=42), n_features_to_select=2, step=1)
X_train_rfe = sel.fit_transform(X_train, y_train)
X_test_rfe = sel.transform(X_test)
acc_rfe = evaluate_model(X_train_rfe, X_test_rfe, y_train, y_test)
# 5. Tree-based feature selection
clf = ExtraTreesClassifier(n_estimators=50, random_state=42)
clf.fit(X_train, y_train)
model = SelectFromModel(clf, prefit=True)
X_train_tree = model.transform(X_train)
X_test_tree = model.transform(X_test)
acc_tree = evaluate_model(X_train_tree, X_test_tree, y_train, y_test)

accuracy_results = {
    "No Feature Selection": acc_no_selection,
    "Variance Threshold": acc_variance_threshold,
    "SelectKBest": acc_select_kbest,
    "RFE": acc_rfe,
    "Tree-based": acc_tree
}

def get_accuracies():
    return accuracy_results

def get_accuracies():
    return {"No Feature Selection": 0.5}

def get_accuracies():
    return {k: v for k, v in locals().get("accuracy_results", {}).items()}