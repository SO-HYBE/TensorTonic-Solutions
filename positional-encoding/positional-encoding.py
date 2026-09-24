import numpy as np

def positional_encoding(seq_len: int, d_model: int, base: float = 10000.0) -> np.ndarray:
    """
    Returns a NumPy array of shape (seq_len, d_model).
    """
    # Write code here
    pe_output = np.zeros((seq_len, d_model))
    
    for pos in range(seq_len):
        for i in range(0, d_model, 2):
            if i + 1 < d_model:
                sin_val = np.sin(pos / (base ** ((i)/d_model)))
                pe_output[pos,i] = sin_val
                cos_val = np.cos(pos / (base ** ((i)/d_model)))
                pe_output[pos,i+1] = cos_val
            else:
                sin_val = np.sin(pos / (base ** ((i)/d_model)))
                pe_output[pos,i] = sin_val
    
    return pe_output