def popularity_ranking(items: list, min_votes: int, global_mean: float) -> list:
    """
    Returns the weighted rating for every item.
    """
    # Write code here
    WR = []
    for item in items:
        rating = item[0]
        vote_count = item[1]

        item_wr = ((vote_count / (vote_count + min_votes)) * rating) + ((min_votes / (vote_count + min_votes)) * global_mean)

        WR.append(item_wr)

    return WR