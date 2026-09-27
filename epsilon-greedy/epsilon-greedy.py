import numpy as np

def epsilon_greedy(q_values: list, epsilon: float, seed: int = 0) -> int:
    """
    Returns the action index as an integer.
    """
    # Write code here
    rng = np.random.default_rng(seed = seed)

    u = rng.random()

    if u < epsilon:
        a = int(rng.integers(len(q_values)))
    else:
        a = int(np.argmax(q_values))

    return a
    