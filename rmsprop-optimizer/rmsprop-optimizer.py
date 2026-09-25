import numpy as np

def rmsprop_step(
    w: list,
    g: list,
    s: list,
    lr: float = 0.001,
    beta: float = 0.9,
    eps: float = 1e-8,
) -> tuple[list, list]:
    """
    Returns (new_w, new_s) with the same shapes as the inputs.
    """
    # Write code here
    st = beta * np.array(s, dtype = float) + (1 - beta) * (np.array(g, dtype = float) ** 2)
    wt = np.array(w, dtype = float) - lr * (g/np.sqrt(st + eps))

    return (list(wt), list(st))