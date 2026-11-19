def min_max_scaling(data: list) -> list:
    """
    Returns each data column scaled to the range from 0 through 1.
    """
    # Write code here
    scaled = [[0 for i in range(len(data[0]))] for i in range(len(data))]
    mins = [min(col) for col in zip(*data)]
    maxs = [max(col) for col in zip(*data)]
    for j in range(len(data[0])):
        for i in range(len(data)):
            if mins[j] == maxs[j]:
                scaled[i][j] = 0.0
            else:
                scaled[i][j] = (data[i][j] - mins[j])/(maxs[j]-mins[j])
    return scaled