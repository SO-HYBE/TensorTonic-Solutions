import numpy as np

def e_means(X: list, centroids: list, batches: list, alpha: float) -> dict:
    """
    Returns a dict with the final centroids (k, d), the running counts (k,), the labels (n,) and the mse.
    """
    X = np.asarray(X)
    centroids = np.asarray(centroids, dtype = np.float64)
    k = centroids.shape[0]
    S = np.array(centroids, copy = True, dtype = np.float64)
    N = np.ones((k))
    label_ref = np.arange(k)
    labels = np.zeros((X.shape[0]), dtype = int)
    for batch in batches:
        s = np.zeros((centroids.shape))
        n = np.zeros((k))
        for i in batch:
            labels[i] = np.argmin(np.sum((X[i] - centroids)**2, axis = 1), axis = 0, keepdims = False)

            s[labels[i]] += X[i]
            n[labels[i]] += 1

        S = ((1 - alpha) * S) + (alpha * s)
        N = ((1 - alpha) * N) + (alpha * n)

        centroids[N > 0] = S[N > 0] / N[N > 0][:, None]        
    out = np.zeros((X.shape))
    
    dist = ((X[:, None, :] - centroids[None, :, :]) ** 2).sum(axis=-1)
    out = np.argmin(dist, axis = 1)

    mse = float(dist[np.arange(X.shape[0]), out].mean())

    return {"centroids" : centroids, "counts": N, "labels": out, "mse": mse}