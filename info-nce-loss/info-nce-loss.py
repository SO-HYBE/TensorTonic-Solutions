import numpy as np

def info_nce_loss(Z1: list, Z2: list, temperature: float = 0.1) -> float:
    """
    Returns the loss as a float.
    """
    # Write code here
    Z1 = np.asarray(Z1)
    Z2 = np.asarray(Z2)
    N = Z1.shape[0]
    S = np.dot(Z1, Z2.T) / temperature
    maxes = np.max(S, axis=1, keepdims=True)
    S = S - maxes
    sum = 0
    for i in range(N):
        sum += (np.sum(np.log(np.exp(S[i][i]) / np.sum(np.exp(S[i])))))
    return float(-(1 / N) * sum)