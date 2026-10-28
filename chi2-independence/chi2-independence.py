import numpy as np

def chi2_independence(C: list) -> dict:
    """
    Returns a dictionary with chi2 and expected.
    """
    # Write code here
    counts = np.asarray(C)
    expected = np.zeros((counts.shape))
    R = np.sum(counts, axis = 1)
    C = np.sum(counts, axis = 0)
    N = np.sum(R)
    for i in range(len(R)):
        for j in range(len(C)):
            expected[i][j] = (R[i] * C[j]) / N
            
    chi = float(np.sum(np.power(counts - expected, 2) / expected))

    return {"chi2":chi, "expected":expected}

        
    