import numpy as np

def lbfgs_direction(grad: list, s_list: list, y_list: list) -> list:
    """
    Returns the L-BFGS descent direction from the stored history.
    """
    # Write code here
    m = len(s_list)
    s = np.asarray(s_list, dtype = float)
    y = np.asarray(y_list, dtype = float)
    g = np.asarray(grad, dtype = float)
    alpha = np.zeros(m) 
    p = np.zeros(m)
    beta = np.zeros(m)

    for i in range(m):
        p[i] = 1 / (y[i].T @ s[i])
        
    q = g.copy()
    for i in range(m-1, -1, -1):
        alpha[i] = p[i] * s[i].T @ q
        q = q - alpha[i] * y[i]

        if i == m-1:
            gamma = (s[i].T @ y[i]) / (y[i].T @ y[i])

    r = gamma * q

    for i in range(m):
        beta[i] = p[i] * y[i].T @ r
        r = r + s[i] * (alpha[i] - beta[i])
    r = -r
    return r.tolist()
    