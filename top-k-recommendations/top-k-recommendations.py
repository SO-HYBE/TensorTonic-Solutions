def top_k_recommendations(scores: list, rated_indices: list, k: int) -> list:
    """
    Returns the highest-scoring unrated item indices.
    """
    # Write code 
    fil = []
    for  i in range(len(scores)):
        if i not in rated_indices:
            fil.append(i)
    fil.sort(key=lambda i: (-scores[i], i))
    return fil[:k]