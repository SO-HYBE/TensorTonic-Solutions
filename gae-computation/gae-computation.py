def gae(rewards: list, values: list, gamma: float, lam: float) -> list:
    """
    Returns the generalized advantage estimate at every timestep.
    """
    # Write code here
    A = [0 for i in range(len(rewards))]
    delta_T = []
    for t in range(len(rewards)):
        delta_t = rewards[t] + (gamma * values[t + 1]) - values[t]
        delta_T.append(delta_t)
    A[len(rewards) -1] = delta_T[len(rewards)-1]
    for t in range(len(rewards) - 2, -1, -1):
        A[t] = delta_T[t] + (gamma * lam * A[t+1])

    return A