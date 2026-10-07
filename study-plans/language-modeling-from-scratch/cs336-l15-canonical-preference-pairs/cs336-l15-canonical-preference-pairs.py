def canonical_preference_pairs(records: list) -> dict:
    """
    Returns a dict with pairs: a list of prompt_id, winner_id, loser_id dictionaries.
    """

    pairs = []
    
    for record in records:
        sorted_cand = sorted(record["candidates"], key=lambda c: c["rank"])
        for i in range(len(sorted_cand) - 1):
            for j in range(i + 1, len(sorted_cand)):
                if sorted_cand[i]["rank"] < sorted_cand[j]["rank"]:
                    pairs.append({"prompt_id":record["prompt_id"], "winner_id":sorted_cand[i]["id"], "loser_id":sorted_cand[j]["id"]})
                
    return {"pairs": pairs}