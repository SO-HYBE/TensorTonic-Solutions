import numpy as np

def apply_homogeneous_transform(T: list, points: list) -> np.ndarray:
    """
    Returns transformed points with shape (3,) or (N, 3).
    """
    # Write code here
    points_arr = np.array(points)
    T_arr = np.array(T)
    
    if isinstance(points[0], list):
        points_h = np.append(points_arr, np.ones((points_arr.shape[0], 1)), axis = 1)
        points_h = points_h.T
        points_trans = T_arr @ points_h
        output = points_trans[:3,].T   
    else:
        points_h = np.append(points_arr, 1)
        points_h = points_h.T
        points_trans = T_arr @ points_h
        output = points_trans[:3,]

    return output
        