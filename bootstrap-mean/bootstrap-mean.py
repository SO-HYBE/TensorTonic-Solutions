import numpy as np

def bootstrap_mean(x: list, n_bootstrap: int = 1000, ci: float = 0.95, seed: int = 0) -> dict:
    """
    Returns a dictionary with bootstrap_mean, lower, and upper.
    """
    # Write code here
    x_arr = np.asarray(x)
    rng = np.random.default_rng(seed)
    og_mean = np.mean(x_arr)

    sample_means = []
    for i in range(n_bootstrap):
        sample = rng.choice(x_arr, size = x_arr.shape, replace = True)
        sample_mean = np.mean(sample)
        sample_means.append(sample_mean)
        
    sample_means.sort()
    lower_percentile = ((1 - ci) / 2) * 100
    upper_percentile = (ci + ((1 - ci) / 2)) * 100

    lower_bound = np.percentile(sample_means, lower_percentile)
    upper_bound = np.percentile(sample_means, upper_percentile)

    
    return {"bootstrap_mean": np.mean(np.asarray(sample_means)), "lower": lower_bound, "upper": upper_bound}
        
        