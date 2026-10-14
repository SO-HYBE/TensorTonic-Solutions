import numpy as np

def gru_cell_forward(x: list, h_prev: list, params: dict) -> np.ndarray:
    """
    Returns the updated hidden state as a NumPy array matching the shape of h_prev.
    """
    # Write code here
    x = np.asarray(x)
    h_prev = np.asarray(h_prev)

    zt = 1 / (1 + np.exp(-(np.dot(x , params["Wz"]) + np.dot(h_prev , params["Uz"]) + params["bz"])))
    rt = 1 / (1 + np.exp(-(np.dot(x , params["Wr"]) + np.dot(h_prev , params["Ur"]) + params["br"])))

    cand_ht = np.tanh(np.dot(x , params["Wh"]) + np.dot((rt * h_prev) , params["Uh"]) + params["bh"])

    ht = ((1 - zt) * h_prev) + (zt * cand_ht)

    return ht