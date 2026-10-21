import numpy as np

def adadelta_step(w: list, grad: list, E_grad_sq: list, E_update_sq: list, rho: float = 0.9, eps: float = 1e-6) -> dict:
    """
    Returns a dictionary with new_w, new_E_grad_sq, and new_E_update_sq.
    """
    # Write code here
    w = np.asarray(w)
    grad = np.asarray(grad)
    E_grad_sq = np.asarray(E_grad_sq)
    E_update_sq = np.asarray(E_update_sq)

    E_grad_new = rho * E_grad_sq + ((1-rho) * (grad ** 2)) 

    param_change = -(np.sqrt(E_update_sq + eps)/np.sqrt(E_grad_new + eps)) * grad

    E_update_new = rho * E_update_sq + ((1-rho) * (param_change ** 2))

    w_new = w + param_change

    return {"new_w":w_new, "new_E_grad_sq": E_grad_new, "new_E_update_sq": E_update_new}