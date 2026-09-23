import numpy as np

def pad_sequences(seqs: list, pad_value: int = 0, max_len: int | None = None) -> np.ndarray:
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    # Your code here
    if max_len is None:
        max_len = len(max(seqs, key=len, default=[]))

    if len(seqs) == 0:
        return np.empty((0,0), dtype = np.int32)
    for seq in seqs:
        while len(seq) != max_len:
            if len(seq) < max_len:
                seq.append(pad_value)
            elif len(seq) > max_len:
                seq.pop()
            else:
                break

    return np.array(seqs, dtype = np.int32)
    