import numpy as np

def knn_distance(X_train: list, X_test: list, k: int) -> np.ndarray:
    """
    Returns a NumPy array with shape (n_test, k).
    """
    # Write code here
    X_train = np.asarray(X_train)
    X_test = np.asarray(X_test)
    if X_train.ndim == 1:
        X_train = X_train.reshape(-1, 1)
    if X_test.ndim == 1:
        X_test = X_test.reshape(-1, 1)
    d = np.argsort(np.sqrt(np.sum((X_test[:, None, :] - X_train[None, :, :]) ** 2, axis = -1)), kind='stable')
    d = d[:, :k]
    if k > len(X_train):
        pad_len = k - len(X_train)
        padding = np.full((len(X_test), pad_len), -1, dtype=int)
        d = np.concatenate([d, padding], axis=1)
    return d