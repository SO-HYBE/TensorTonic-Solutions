def policy_gradient_loss(log_probs: list, rewards: list, gamma: float) -> float:
    """
    Returns the REINFORCE loss with a mean-return baseline.
    """
    # Write code here
    T = len(log_probs)
    G = [0] * T
    sum = 0
    for t in range(T - 1, -1, -1):
        if t == T - 1:
            G[T-1] = rewards[T-1]
        else:
            G[t] = (rewards[t] + (gamma * G[t+1]))
        
        sum += G[t]

    G_mean = sum / T
    A = [val - G_mean for val in G]

    l_sum = 0
    for t in range(T):
        l_sum += log_probs[t] * A[t]
    return - (1/T) * l_sum

    