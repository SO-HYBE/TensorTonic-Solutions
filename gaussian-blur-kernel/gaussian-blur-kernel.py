import math

def gaussian_kernel(size: int, sigma: float) -> list:
    """
    Returns a square two-dimensional list.
    """
    # Write code here
    cy = int(size/2)
    cx = int(size/2)

    output = [[0 for i in range(size)] for j in range(size)]
    sum = 0
    for c in range(size):
        for r in range(size):

            x = c - cx
            y = cy - r
            G_xy = math.exp(-(x**2 + y **2)/(2 * sigma ** 2))

            output[c][r] = G_xy
            sum += G_xy
            
    for c in range(size):
        for r in range(size):
            output[c][r] = output[c][r] / sum
            
    return(output)
            