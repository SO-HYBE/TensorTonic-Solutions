import math

def binary_focal_loss(predictions: list, targets: list, alpha: float, gamma: float) -> float:
    """
    Returns the mean binary focal loss as a float.
    """
    # Write code here
    sum = 0
    for i, pred in enumerate(predictions):
        if targets[i] == 1:
            pt = pred
        else:
            pt = 1 - pred
        FL = -alpha * ((1 - pt) ** gamma) * math.log(pt)
        sum += FL
    return sum / len(predictions)