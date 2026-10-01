def precision_recall_at_k(recommended: list, relevant: list, k: int) -> list[float]:
    """
    Returns [precision, recall] as a list of two floats.
    """
    # Write code here
    top_k = recommended[:k]
    intersect = len(list(set(top_k) & set(relevant)))
    precision = intersect / k
    recall = intersect / len(relevant)

    return [precision, recall]