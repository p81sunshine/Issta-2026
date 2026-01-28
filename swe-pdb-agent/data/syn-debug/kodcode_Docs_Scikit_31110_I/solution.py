import matplotlib.pyplot as plt
from sklearn.model_selection import validation_curve, learning_curve
from sklearn.model_selection import ValidationCurveDisplay, LearningCurveDisplay

def plot_model_diagnostics(dataset_function, model, param_name, param_range, train_sizes, cv):
    """
    Loads a dataset, trains a machine learning model, generates and plots validation and learning curves.
    
    Args:
    dataset_function: function returning features (X) and labels (y) of the dataset
    model: a scikit-learn estimator object
    param_name: str, name of the hyperparameter to vary for the validation curve
    param_range: list or array, values of the hyperparameter to vary
    train_sizes: list, sizes of the training samples for the learning curve
    cv: int, number of folds for cross-validation

    Returns:
    Displays two plots: validation curve and learning curve
    """
    # Load dataset
    X, y = dataset_function()

    # Generate validation curve
    train_scores, valid_scores = validation_curve(
        model, X, y, param_name=param_name, param_range=param_range, cv=cv)

    # Plot validation curve
    plt.figure()
    ValidationCurveDisplay.from_estimator(
        model, X, y, param_name=param_name, param_range=param_range, cv=cv)
    plt.title("Validation Curve")
    plt.xlabel(param_name)
    plt.ylabel("Score")
    plt.show()

    # Generate learning curve
    train_sizes, train_scores, valid_scores = learning_curve(
        model, X, y, train_sizes=train_sizes, cv=cv)
    
    # Plot learning curve
    plt.figure()
    LearningCurveDisplay.from_estimator(
        model, X, y, train_sizes=param_range, cv=cv)
    plt.title("Learning Curve")
    plt.xlabel("Training examples")
    plt.ylabel("Score")
    plt.show()

    model.set_params(**{param_name: param_range[-1]})

    return model