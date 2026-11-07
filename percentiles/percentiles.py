import numpy as np

def percentiles(x: list, q: list) -> np.ndarray:
    """
    Returns a NumPy array of percentiles.
    """
    # Write code here
    n = len(x)
    x = np.asarray(x)
    sorted = np.sort(x)
    output = []
    for val in q:
        r = (val/100)* (n - 1)
        l = int(np.floor(r))
        u = int(np.ceil(r))
        w = r - l
        p_q = (1 - w) * sorted[l] + w * sorted[u]
        
        output.append(p_q)
    return np.asarray(output)
    