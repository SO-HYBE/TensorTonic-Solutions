import numpy as np

def pearson_correlation(X: list) -> np.ndarray:
    """
    Returns the correlation matrix as a NumPy array.
    """
    # Write code here
    X = np.asarray(X)
    N = X.shape[0]
    centered = X - np.mean(X, axis = 0)
    cov = (centered.T @ centered) / (N-1)
    den = np.sqrt(np.diag(cov))

    corr = cov / (np.outer(den, den))
    return corr