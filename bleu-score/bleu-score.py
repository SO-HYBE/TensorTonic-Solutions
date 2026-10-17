import math
from collections import Counter

def bleu_score(candidate: list, reference: list, max_n: int) -> float:
    """
    Returns the unsmoothed BLEU score.
    """
    # Write code here
    n = 1
    precisions = []
        
    while n < max_n + 1:
        if n == 1:
            cand_count = Counter(candidate)
            ref_count = Counter(reference)
        else:
            cand_slices = [candidate[i:] for i in range(n)]            
            ref_slices = [reference[i:] for i in range(n)]       
    
            zipped_cand = zip(*cand_slices)
            zipped_ref = zip(*ref_slices)
            
            cand_count = Counter(zipped_cand)
            ref_count = Counter(zipped_ref)
            
        num = 0
        den = 0

        if len(candidate) > 0:
            for key, value in cand_count.items():
                num += min(cand_count[key], ref_count[key])
                den += cand_count[key]
            precisions.append(num / den)

        else:
            return 0

        n+=1

    if 0 in precisions:
        return 0
        
    BP = 1 if len(candidate) >= len(reference) else math.exp(1-(len(reference)/len(candidate)))
    log_prec = [math.log(prec) for prec in precisions]
    BLEU = BP * math.exp(1/max_n * sum(log_prec))

    return BLEU