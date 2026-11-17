import numpy as np

def svd_2x2_singular_values(A: np.ndarray) -> tuple:
    """
    Compute SVD of a 2x2 matrix using one Jacobi rotation.
    
    Args:
        A: A 2x2 numpy array
    
    Returns:
        Tuple (U, S, Vt) where A ≈ U @ diag(S) @ Vt
        - U: 2x2 orthogonal matrix
        - S: length-2 array of singular values
        - Vt: 2x2 orthogonal matrix (transpose of V)
    """
    A = np.asarray(A, dtype=float)
    ATA = A.T @ A
    
    b_val = ATA[0, 1]
    diff = ATA[0, 0] - ATA[1, 1]
    
    if b_val == 0 and diff == 0:
        theta = 0.0
    else:
        theta = 0.5 * np.arctan2(2 * b_val, diff)
        
    c = np.cos(theta)
    s = np.sin(theta)
    
    V = np.array([
        [c, -s],
        [s,  c]
    ])
    
    D = V.T @ ATA @ V
    s_vals = np.sqrt(np.maximum(0, np.diagonal(D)))
    
    U = (A @ V) / s_vals
    Vt = V.T
    
    if s_vals[0] < s_vals[1]:
        s_vals = s_vals[::-1]
        U = U[:, ::-1]
        Vt = Vt[::-1, :]
        
    return (U, s_vals, Vt)
