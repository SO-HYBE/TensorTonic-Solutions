import torch
import triton
import triton.language as tl


@triton.jit
def layernorm_bwd_kernel(
    x_ptr, gamma_ptr, dy_ptr,
    dx_ptr, dgamma_ptr, dbeta_ptr,
    stride_x_row, stride_dy_row, stride_dx_row,
    N, eps,
    BLOCK_SIZE: tl.constexpr,
):
    # Write code here
    col_off = tl.arange(0, BLOCK_SIZE)
    mask = col_off < N
    pid = tl.program_id(axis = 0)
    x_val = tl.load(x_ptr + pid * stride_x_row + col_off, mask=mask, other=0.0)
    dy_val = tl.load(dy_ptr + pid * stride_dy_row + col_off, mask=mask, other=0.0)
    gamma = tl.load(gamma_ptr + col_off, mask=mask, other=0.0)
    mean_i = tl.sum(x_val) / N
    centered_x = tl.where(mask, x_val - mean_i, 0.0)
    sq_difference = centered_x * centered_x
    sum_sq_diff = tl.sum(sq_difference, axis=0)
    variance = sum_sq_diff / N
    rstd = 1 / tl.sqrt(variance + eps)
    x_hat = centered_x * rstd
    dy_norm = dy_val * gamma
    c1 = tl.sum(dy_norm, axis = 0) / N
    c2 = tl.sum(dy_norm * x_hat, axis = 0) / N
    dx = tl.store(dx_ptr + pid * stride_dx_row + col_off, rstd * (dy_norm - c1 - x_hat * c2), mask = mask)
    dgamma = dy_val * x_hat
    dbeta = dy_val
    tl.atomic_add(dgamma_ptr + col_off, dgamma, mask=mask)
    tl.atomic_add(dbeta_ptr + col_off, dbeta, mask=mask)
def solve(
    x: torch.Tensor, gamma: torch.Tensor, dy: torch.Tensor,
    dx_out: torch.Tensor, dgamma_out: torch.Tensor, dbeta_out: torch.Tensor,
    eps: float,
) -> None:
    """Launch the LayerNorm backward kernel: one program per row, atomic reductions for dgamma and dbeta."""
    M, N = x.shape
    BLOCK_SIZE = triton.next_power_of_2(N)
    dgamma_out.zero_()
    dbeta_out.zero_()
    grid = (M,)
    layernorm_bwd_kernel[grid](
        x, gamma, dy,
        dx_out, dgamma_out, dbeta_out,
        x.stride(0), dy.stride(0), dx_out.stride(0),
        N, eps,
        BLOCK_SIZE=BLOCK_SIZE,
    )