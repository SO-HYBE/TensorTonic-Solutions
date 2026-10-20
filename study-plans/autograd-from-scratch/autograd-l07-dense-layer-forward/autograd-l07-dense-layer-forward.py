import torch

def dense_layer_forward(inputs: torch.Tensor, weight_matrix: torch.Tensor, biases: torch.Tensor, nonlinear: bool) -> torch.Tensor:
    """
    Returns an output vector in neuron order, preserving input dtype and device.
    """
    a = torch.zeros(weight_matrix.shape[0], dtype = inputs.dtype, device = inputs.device)
    for idx, weight in enumerate(weight_matrix):
        a[idx] = torch.dot(weight, inputs) + biases[idx]
        
    if nonlinear:
        a = torch.tanh(a)

    return a