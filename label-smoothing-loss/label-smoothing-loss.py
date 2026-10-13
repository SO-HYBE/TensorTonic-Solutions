import math

def label_smoothing_loss(predictions: list, target: int, epsilon: float) -> float:
    """
    Returns cross-entropy loss for the smoothed target distribution.
    """
    # Write code here
    L = 0.0
    qis = []
    for i in range(len(predictions)):
        if i == target:
            qi = (1 - epsilon) + (epsilon / len(predictions))
        else:
            qi = epsilon / len(predictions)
        
        qis.append(qi)
        
    for i in range(len(predictions)):
        if predictions[i] != 0:
            L += qis[i] * math.log(predictions[i])

    return -L