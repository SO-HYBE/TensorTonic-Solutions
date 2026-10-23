import math
def conv2d(image: list, kernel: list, stride: int = 1, padding: int = 0) -> list:
    """
    Returns a two-dimensional list.
    """
    # Write code here
    K = len(kernel)
    H = len(image)
    W = len(image[0])
    
    if padding != 0: 
        for i in range(padding):
            for r in image:
                r.insert(0, 0)
                r.append(0)     
        image.insert(0, [0] * len(image[0]))
        image.append([0] * len(image[0]))

    H_out = math.floor((H + (2 * padding - K)) / stride) + 1
    W_out = math.floor((W + (2 * padding - K)) / stride) + 1

    output = [[0 for c in range(W_out)] for r in range(H_out)]

    for i in range(H_out):
        for j in range(W_out):
            for m in range(K):
                for n in range(len(kernel[0])):
                    output[i][j] += image[(i * stride)+ m][(j * stride) + n] * kernel[m][n]

    return output
    