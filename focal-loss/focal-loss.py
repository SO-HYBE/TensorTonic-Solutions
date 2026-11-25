import numpy as np

def focal_loss(p: list, y: list, gamma: float = 2.0) -> float:
    """
    Returns the loss as a float.
    """
    # Write code here
    p = np.clip(np.asarray(p), np.finfo(np.float32).eps, 1 - np.finfo(np.float32).eps)
    y = np.asarray(y)

    L = - ((1 - p) ** gamma) * (y * np.log(p)) - (p ** gamma) * (1 - y) * np.log(1 - p)

    return float(np.mean(L))
    