def train_bpe(corpus: list[str], vocab_size: int) -> dict:
    seqs = [list(text.encode("utf-8")) for text in corpus]
    token_bytes = [bytes([i]) for i in range(256)]
    vocab = []
    merges = []

    while len(token_bytes) < vocab_size:
        counts = {}
        for seq in seqs:
            for k in range(len(seq) - 1):
                pair = (seq[k], seq[k + 1])
                counts[pair] = counts.get(pair, 0) + 1
        if not counts:
            break

        best = max(counts, key=lambda p: (counts[p], token_bytes[p[0]], token_bytes[p[1]]))

        new_id = len(token_bytes)
        token_bytes.append(token_bytes[best[0]] + token_bytes[best[1]])
        merges.append([best[0], best[1], new_id])
        vocab.append([new_id, list(token_bytes[new_id])])

        new_seqs = []
        for seq in seqs:
            out = []
            k = 0
            while k < len(seq):
                if k < len(seq) - 1 and seq[k] == best[0] and seq[k + 1] == best[1]:
                    out.append(new_id)
                    k += 2
                else:
                    out.append(seq[k])
                    k += 1
            new_seqs.append(out)
        seqs = new_seqs

    return {"vocab": vocab, "merges": merges}