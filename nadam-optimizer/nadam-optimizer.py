import numpy as np

def nadam_step(w: list, m: list, v: list, grad: list, lr: float = 0.002, beta1: float = 0.9, beta2: float = 0.999, eps: float = 1e-8) -> dict:
    """
    Returns a dictionary with new_w, new_m, and new_v.
    """
    # Write code here
    w = np.asarray(w)
    m = np.asarray(m)
    v = np.asarray(v)
    grad = np.asarray(grad)

    mt = (beta1 * m) + (1 - beta1) * grad
    vt = (beta2 * v) + (1 - beta2) * (grad**2)
    m_nest = (beta1 * mt) + (1-beta1) * grad 

    wt = w - (lr * (m_nest /(vt ** 0.5) + eps))

    return {"new_w":wt, "new_m":mt, "new_v":vt}
    