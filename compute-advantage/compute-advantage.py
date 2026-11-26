import numpy as np

def compute_advantage(states: list, rewards: list, V: list, gamma: float) -> np.ndarray:
    """
    Returns the advantages as a NumPy array.
    """
    # Write code here
    states = np.asarray(states)
    rewards = np.asarray(rewards)
    V = np.asarray(V)
    T = len(rewards)
    G = np.zeros((rewards.shape))
    A = np.zeros((rewards.shape))
    G[T-1] = rewards[T-1]
    for t in range(T-2, -1, -1):
        G[t] = rewards[t] + (gamma * G[t+1])

    for t in range(T):
        A[t] = G[t] - V[states[t]]
        
    return np.round(A, 4)