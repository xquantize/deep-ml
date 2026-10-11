import numpy as np

def pca(data: np.ndarray, k: int) -> np.ndarray:
    """
    Perform PCA and return the top k principal components.
    
    Args:
        data: Input array of shape (n_samples, n_features)
        k: Number of principal components to return
    
    Returns:
        Principal components of shape (n_features, k), rounded to 4 decimals.
        Each eigenvector's sign is fixed so its first non-zero element is positive.
    """
    # Your code here
    #centered_data = data - np.mean(data, axis=0)
    mean = np.mean(data, axis=0)
    std = np.std(data, axis=0)
    std_safe = np.where(std == 0, 1.0, std)
    data_std = (data - mean) / std_safe

    cov_matrix = np.cov(data_std, rowvar=False)
    eigenvalues, eigenvectors = np.linalg.eigh(cov_matrix)

    sorted_idx = np.argsort(eigenvalues)[::-1]
    eigenvectors = eigenvectors[:, sorted_idx]
    top_k_eigenvectors = eigenvectors[:, :k]

    for i in range(top_k_eigenvectors.shape[1]):
        col = top_k_eigenvectors[:, i]
        nonzero_idx = np.nonzero(col)[0]

        if len(nonzero_idx) > 0 and col[nonzero_idx[0]] < 0:
            top_k_eigenvectors[:, i] = -col

    return np.round(top_k_eigenvectors, 4)
