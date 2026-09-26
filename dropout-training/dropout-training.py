import numpy as np

def dropout(
    x: list,
    p: float = 0.5,
    rng: np.random.Generator = None,
) -> tuple[np.ndarray, np.ndarray]:
    """
    Returns (output, dropout_pattern) as NumPy arrays matching the shape of x.
    """
    # Write code here
    x = np.array(x, dtype = float)
    
    if rng is None:
        rand_arr = np.random.random(x.shape)
    else:
        rand_arr = rng.random(x.shape)
    
    mask = (rand_arr >= p) * (1/(1-p))

    do_x = x * mask

    return (do_x, mask)
