import numpy as np

def mc_policy_evaluation(episodes: list, gamma: float, n_states: int) -> np.ndarray:
    """
    Returns the state values as a NumPy array.
    """
    # Write code here
    G = np.zeros((len(episodes[0])))
    sum = np.zeros((n_states))
    count = np.zeros((n_states))
    for episode in episodes:  
        running = 0
        G = np.zeros(len(episode))
        for t, (state, reward) in enumerate(reversed(episode)):
                running = reward + gamma * running
                G[t] = running
        rev_G = G[::-1]
        seen = set()
        for i, (state, reward) in enumerate(episode):
            if state in seen:
                continue
            else:
                seen.add(state)
                sum[state] += rev_G[i]
                count[state] += 1
    out = np.zeros((n_states))
    out[count > 0] = sum[count > 0] / count[count > 0]
    
    return np.round(out, 4)