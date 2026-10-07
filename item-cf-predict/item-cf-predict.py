def item_cf_predict(user_ratings: list, item_similarities: list, target: int) -> float:
    """
    Returns the similarity-weighted rating prediction.
    """
    # Write code here
    user_ratings.pop(target)
    item_similarities.pop(target)

    for idx, val in enumerate(user_ratings):
        if user_ratings[idx] == 0 or item_similarities[idx] < 0:
            user_ratings.pop(idx)
            item_similarities.pop(idx)
    print(user_ratings)

    num = 0
    den = 0
    for idx, val in enumerate(user_ratings):
        num += (val * item_similarities[idx])
        den += (item_similarities[idx])

    if den == 0:
        return 0.0
    else:
        rating = num/den
    
    return rating
    