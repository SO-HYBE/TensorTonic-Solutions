def cumulative_returns(returns: list) -> list:
    """
    Returns the compounded cumulative return after every period.
    """
    # Write code here
    cum_returns = []
    prev = 0.0
    
    for ret in returns:
        Wt = (1 + prev) * (1+ret)
        cum_returns.append(Wt - 1)
        prev = Wt - 1

    return cum_returns
    