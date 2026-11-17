import numpy as np

def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
    A = np.asarray(A, dtype=float)
    b = np.asarray(b, dtype=float)
    
    num_rows = len(b)
    x = np.zeros(num_rows)
    
    for _ in range(n):
        x_new = np.zeros_like(x)

        for i in range(num_rows):
            off_diagonal_sum = sum(A[i, j] * x[j] for j in range(num_rows) if j != i)
            x_new[i] = (b[i] - off_diagonal_sum) / A[i, i]
        x = x_new
        
    return [round(float(val), 4) for val in x]
