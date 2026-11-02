import torch

def kv_cache_decode_step(
    query: torch.Tensor, new_key: torch.Tensor, new_value: torch.Tensor,
    key_cache: torch.Tensor, value_cache: torch.Tensor,
    num_query_heads: int, num_kv_heads: int,
) -> dict:
    """
    Returns a dict of tensors: output, new_key_cache, new_value_cache.
    """
    G = num_query_heads // num_kv_heads
    D = query.shape[2]
    B = query.shape[0]
    key = torch.cat((key_cache, torch.unsqueeze(new_key, dim=2)), dim = 2)
    value = torch.cat((value_cache, torch.unsqueeze(new_value, dim=2)), dim = 2)
    a = torch.softmax(query.reshape(B, num_kv_heads, G, D).float() @ key.transpose(-2, -1).float() / (D ** 0.5), dim = -1)
    y = (a @ value.float()).reshape(B, num_query_heads, D).to(query.dtype)

    return {"output":y, "new_key_cache":key, "new_value_cache":value}