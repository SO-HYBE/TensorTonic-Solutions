import numpy as np

def wasserstein_critic_loss(real_scores: list, fake_scores: list) -> float:
    """
    Returns the loss as a float.
    """
    # Write code here
    Nr = len(real_scores)
    Nf = len(fake_scores)
    real = np.asarray(real_scores)
    fake = np.asarray(fake_scores)

    Loss = 1/Nf * (np.sum(fake)) - 1/Nr * (np.sum(real))

    return float(Loss)