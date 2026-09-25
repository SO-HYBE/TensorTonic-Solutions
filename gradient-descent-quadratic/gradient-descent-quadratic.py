def gradient_descent_quadratic(a: float, b: float, c: float, x0: float, lr: float, steps: int) -> float:
    """
    Returns the final scalar x after the requested iterations.
    """
    # Write code here
    for step in range(steps):
        if step == 0:
            x = x0 - lr * ((2 * a * x0) + b)
        else:
            x = x - lr * ((2 * a * x) + b)

    return x