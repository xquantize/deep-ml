import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
    try:
        A_arr = np.array(A, dtype=float)
        T_arr = np.array(T, dtype=float)
        S_arr = np.array(S, dtype=float)
        
        if A_arr.ndim != 2 or T_arr.ndim != 2 or S_arr.ndim != 2:
            return -1
            
        m, n = A_arr.shape
        t_rows, t_cols = T_arr.shape
        s_rows, s_cols = S_arr.shape
        
        if t_rows != t_cols or t_rows != m:
            return -1
        if s_rows != s_cols or s_cols != n:
            return -1
            
        T_inv = np.linalg.inv(T_arr)
        _ = np.linalg.inv(S_arr)
        
        transformed = T_inv @ A_arr @ S_arr
        
        return transformed.tolist()
        
    except (np.linalg.LinAlgError, ValueError, TypeError):
        return -1
