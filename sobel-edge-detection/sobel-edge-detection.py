import math

def sobel_edges(image: list) -> list:
    """
    Returns the zero-padded Sobel gradient magnitude at every pixel.
    """
    # Write code here
    kx = [[-1,0,1],[-2,0,2],[-1,0,1]]
    ky = [[-1,-2,-1],[0,0,0],[1,2,1]]

    new_col = len(image[0]) + 2

    H = len(image)
    W = len(image[0])
    result = [[0] * W for _ in range(H)]
    padded_image = [[0] + row + [0] for row in image]    
    
    padded_image.insert(0, [0] * new_col)
    padded_image.append([0] * new_col)
    
    for i in range(1, H + 1):
        for j in range(1, W + 1):
            gx = 0
            gy = 0
            
            for a in range(-1,2):
                for b in range(-1,2):
                    pixel = padded_image[i + a][j + b] 
                    gx += kx[a + 1][b + 1] * pixel
                    gy += ky[a + 1][b + 1] * pixel
    
            g_mag = math.sqrt(gx**2 + gy**2)
            result[i - 1][j - 1] = g_mag

    return result