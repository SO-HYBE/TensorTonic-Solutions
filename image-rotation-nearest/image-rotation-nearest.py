import math

def rotate_image(image: list, angle_degrees: float) -> list:
    """
    Returns the counterclockwise nearest-neighbor rotation.
    """
    # Write code here
    H = len(image)
    W = len(image[0])

    cy = (H - 1) / 2
    cx = (W - 1) / 2
    theta = angle_degrees * (math.pi / 180)

    output = [[0 for j in range(W)] for i in range(H)]
    
    for i in range(H):
        
        for j in range(W):
            dy = i - cy
            dx = j - cx

            sy = cy + (dy * math.cos(theta)) + (dx * math.sin(theta))
            sx = cx - (dy * math.sin(theta)) + (dx * math.cos(theta))

            sy_r = round(sy)
            sx_r = round(sx)

            if sx_r in range(W) and sy_r in range(H):
                output[i][j] = image[sy_r][sx_r]
            else:
                output[i][j] = 0

    return(output)