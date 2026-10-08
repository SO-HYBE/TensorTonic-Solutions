def weighted_moving_average(values: list, weights: list) -> list:
    """
    Returns the weighted average of every complete window.
    """
    # Write code here
    
    wma = []
    for i in range(len(values) - len(weights) + 1):
        num = 0
        den = 0
        for j in range(len(weights)):
            num += (weights[j] * values[i+j])
            den += (weights[j])
        wma.append(num/den)
    return wma