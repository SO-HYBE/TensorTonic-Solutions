import torch

def train_tiny_micrograd_mlp(inputs: torch.Tensor, targets: torch.Tensor, weights: list[torch.Tensor], biases: list[torch.Tensor], learning_rate: float, steps: int) -> tuple:
    """
    Returns final predictions, final loss, trained weights, trained biases, and pre-update loss history.
    """
    history = []
    y = targets.reshape(targets.shape[0], 1)
    weights = [w.detach().clone() for w in weights]
    biases = [b.detach().clone() for b in biases]

    with torch.no_grad():
        for _ in range(steps):
            H = [inputs]
            for l in range(len(weights)):
                H.append(torch.tanh(H[l] @ weights[l].T + biases[l]))

            history.append(torch.sum((H[-1] - y) ** 2))

            G = 2 * (H[-1] - y)
            dWs, dbs = [], []
            for l in reversed(range(len(weights))):
                D = G * (1 - H[l + 1] ** 2)
                dWs.append(D.T @ H[l])
                dbs.append(D.sum(dim=0))
                G = D @ weights[l]
            dWs.reverse()
            dbs.reverse()

            for l in range(len(weights)):
                weights[l] = weights[l] - learning_rate * dWs[l]
                biases[l] = biases[l] - learning_rate * dbs[l]

        H_prev = inputs
        for l in range(len(weights)):
            H_prev = torch.tanh(H_prev @ weights[l].T + biases[l])
        final_loss = torch.sum((H_prev - y) ** 2)

    return (H_prev.reshape(-1), final_loss, weights, biases, history)