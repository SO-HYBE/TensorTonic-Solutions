import numpy as np

def nesterov_momentum_step(w: list, v: list, grad: list, lr: float = 0.01, momentum: float = 0.9) -> dict:
    """
    Returns a dictionary with new_w and new_v.
    """
    # Write code here
    vt = (momentum * np.array(v)) + (lr * np.array(grad))
    wt = np.array(w) - vt

    return {"new_w": wt, "new_v": vt}