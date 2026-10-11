import numpy as np

def batch_generator(X: list, y: list, batch_size: int, seed: int = 42, drop_last: bool = False):
    """
    Returns a generator of (X_batch, y_batch) tuples.
    """
    # Write code here
    rng = np.random.default_rng(seed)
    indices = rng.permutation(len(X))

    X = np.asarray(X)[indices]
    y = np.asarray(y)[indices]

    split_ind = range(batch_size, X.shape[0], batch_size)

    X_batches = np.split(X, split_ind)
    y_batches = np.split(y, split_ind)

    if drop_last:
        num_batches = int(np.floor(X.shape[0]/batch_size))
        X_batches = X_batches[:-1]
        y_batches = y_batches[:-1]
        for i in range(num_batches):
            yield (X_batches[i], y_batches[i])

    else:
        num_batches = int(np.ceil(X.shape[0]/batch_size))
        for i in range(num_batches):
            yield (X_batches[i], y_batches[i])