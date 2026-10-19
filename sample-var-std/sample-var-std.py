import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    # Write code here
    n = len(x)
    x_arr = np.asarray(x)

    variance = float((1 / (n - 1)) * (np.sum((x_arr - np.mean(x_arr))** 2)))
    std = float(np.sqrt(variance))

    return {"variance" : variance, "standard_deviation" : std}