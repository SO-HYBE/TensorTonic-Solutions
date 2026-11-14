def percent_change(series: list) -> list:
    """
    Returns the fractional change between consecutive values.
    """
    # Write code here
    out = []
    for i in range(1, len(series)):
        if series[i-1] == 0:
            out.append(0.0)
        else:
            out.append((series[i] - series[i-1])/series[i-1])
    return out