import math
def binning(values: list, num_bins: int) -> list:
    """
    Returns the equal-width bin index of every value.
    """
    # Write code here
    w = ( max(values) - min(values) )/ num_bins
    return [min(math.floor((val - min(values)) / w), num_bins - 1) if w != 0 else 0 for val in values]