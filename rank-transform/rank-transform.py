from collections import Counter

def rank_transform(values: list) -> list:
    """
    Returns the one-based average rank of every value.
    """
    # Write code here
    sorted_vals = sorted(values)
    sorted_ranks = [i for i in range(1, len(sorted_vals) + 1)]

    final_ranks = []
    rank_map = {}
    if len(values) != len(set(values)):
        counts = Counter(sorted_vals)
        for idx, val in enumerate(sorted_vals):
            if counts.get(val) > 1:
                indexes = [idx for idx, v in enumerate(sorted_vals,start = 1) if v == val]
                for j in range(len(indexes)):
                    sorted_ranks[j] = sum(indexes) / counts.get(val)
                    rank_map[val] = sorted_ranks[j]
            else:
                rank_map[val] = sorted_ranks[idx] 
    else:
        for idx, val in enumerate(sorted_vals):
            rank_map[val] = sorted_ranks[idx]
    for val in values:
        final_ranks.append(rank_map[val])

    return final_ranks