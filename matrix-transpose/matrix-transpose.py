import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    # Write code here
    A = np.array(A)
    w = A.shape[0]
    h = A.shape[1]
    new_A = np.zeros((h, w))
    
    for i in range(w):
        for j in range(h):
            new_A[j][i] = A[i][j]

    return new_A