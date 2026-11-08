import math

def novelty_score(recommendations: list, item_counts: list, n_users: int) -> float:
    """
    Returns the average self-information of the recommended items.
    """
    # Write code here
    sum = 0
    if len(recommendations) == 0:
        return 0.0
    else:
        for i in item_counts:
            sum += (- math.log2(i / n_users))
    return (1 / len(recommendations)) * sum