import numpy as np

def initialize_mcts_edges(policy_logits: np.ndarray, legal_mask: np.ndarray) -> dict:
    """
    Returns: N as an int64 array; W, Q, and P as float64 arrays in a dictionary.
    """
    legal_actions = np.flatnonzero(legal_mask)
    legal_logits = policy_logits[legal_actions]
    m = np.max(legal_logits)

    num = np.exp(legal_logits - m)
    den = np.sum(np.exp(legal_logits - m))
    P = np.zeros_like(policy_logits, dtype=np.float64)
    P[legal_actions] = num / den

    N = np.zeros((policy_logits.shape), dtype = np.int64)
    Q = np.zeros((policy_logits.shape), dtype = np.float64)
    W = np.zeros((policy_logits.shape), dtype = np.float64)

    return {"N": N, "W": W, "Q": Q, "P": P}