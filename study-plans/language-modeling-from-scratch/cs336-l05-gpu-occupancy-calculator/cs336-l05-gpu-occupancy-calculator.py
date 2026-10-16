import math

def gpu_occupancy(
    threads_per_block: int, registers_per_thread: int, shared_mem_per_block: int,
    max_threads_per_sm: int, max_warps_per_sm: int, max_blocks_per_sm: int,
    max_registers_per_sm: int, max_shared_mem_per_sm: int, warp_size: int = 32,
) -> dict:
    """
    Returns a dict: blocks_per_sm (int), resident_warps (int), occupancy (float).
    """
    w = math.ceil(threads_per_block / warp_size)
    eff_threads = w * warp_size
    maxs = []
    
    max_threads = max_threads_per_sm // eff_threads
    if registers_per_thread:
        max_regis = max_registers_per_sm // (registers_per_thread * eff_threads)
        maxs.append(max_regis)
    if shared_mem_per_block :
        max_mem = max_shared_mem_per_sm // shared_mem_per_block
        maxs.append(max_mem)
    max_w = max_warps_per_sm // (w)
    
    maxs.extend([max_threads,max_w])

    b = min(maxs)

    resident_warps = b * w

    occupancy = resident_warps / max_warps_per_sm

    return {"blocks_per_sm": b, "resident_warps": resident_warps, "occupancy": occupancy}
            
