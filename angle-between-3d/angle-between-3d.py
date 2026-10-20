import numpy as np

def angle_between_3d(v: list, w: list) -> float:
    """
    Returns the angle as a float.
    """
    # Write code here
    v = np.asarray(v)
    w = np.asarray(w)

    v_norm = np.sqrt(np.sum(v**2))
    w_norm = np.sqrt(np.sum(w**2))

    if v_norm == 0 or w_norm == 0:
        return np.nan
    else:
        c = np.dot(v,w) / (v_norm * w_norm)
        c = np.clip(c, -1, 1)
        angle = np.arccos(c)
        return float(angle)