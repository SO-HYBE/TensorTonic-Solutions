import numpy as np

def matrix_normalization(matrix: list, axis=None, norm_type: str = "l2") -> np.ndarray:
    """
    Returns a NumPy array with the same shape as matrix.
    """
    # Write code here
    matrix = np.asarray(matrix)
    output = np.zeros((matrix.shape))
    if norm_type == "l1":
        denom = np.sum(np.abs(matrix), axis = axis, keepdims = True)
    elif norm_type == "l2":
        denom = np.sqrt(np.sum(matrix ** 2, axis = axis, keepdims = True))
    elif norm_type == "max":
        denom = np.max(np.abs(matrix), axis = axis, keepdims = True)
    denom = np.where(denom != 0, denom, 1.0)
    output = matrix / denom
    return output
        
        