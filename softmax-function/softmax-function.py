import numpy as np

def softmax(x: list) -> np.ndarray:
    """
    Returns stable softmax probabilities as a NumPy array matching the shape of x.
    """
    # Write code here
    x_arr = np.asarray(x)

    shift_exp = np.exp(x_arr - np.max(x_arr, axis = -1, keepdims = True))
    output = shift_exp / np.sum(shift_exp, axis = -1, keepdims = True)

    return output