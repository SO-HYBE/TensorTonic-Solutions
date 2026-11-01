import math

def elu(x: list, alpha: float = 1.0) -> list:
    """
    Returns ELU applied elementwise to the input values.
    """
    # Write code here
    elu =[ val if val > 0 else alpha * (math.exp(val) - 1) for val in x]
    return elu