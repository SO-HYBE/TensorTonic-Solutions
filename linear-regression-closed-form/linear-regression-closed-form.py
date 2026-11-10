import numpy as np

def linear_regression_closed_form(X: list, y: list) -> list:
    """
    Returns the optimal weight vector as a list.
    """
    # Write code here
    X = np.asarray(X)
    y = np.asarray(y)

    frst = X.T @ X 

    w = np.linalg.pinv(frst) @ (X.T @ y)

    return w