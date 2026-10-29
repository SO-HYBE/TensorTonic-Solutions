def differencing(series: list, order: int) -> list:
    """
    Returns the series after the requested differencing order.
    """
    # Write code here
    current = 0
    temp = series
    while current < order:
        output = []
        for i in range(len(temp) - 1):
            output.append(temp[i+1] - temp[i])
        
        temp = output
        current += 1

    return output