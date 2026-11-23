import numpy as np

def time_based_split(timestamps: list, train_end: int, gap: int, val_end: int) -> dict:
    """
    Returns a dictionary with train_idx and val_idx as sorted integer NumPy arrays.
    """
    times = np.asarray(timestamps)
    train_idx = []
    val_idx = []

    for idx, t in enumerate(timestamps):
        if t < train_end:
            train_idx.append(idx)
        elif t >= (train_end+gap) and t < val_end:
            val_idx.append(idx)
            
            
    return {"train_idx": np.asarray(train_idx), "val_idx": np.asarray(val_idx)}