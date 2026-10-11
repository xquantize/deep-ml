import numpy as np

def get_random_subsets(X, y, n_subsets, replacements=True):
    # Your code here
    n_samples = X.shape[0]
    subsample_size = n_samples if replacements else n_samples // 2
    subsets = []

    for _ in range(n_subsets):
        indices = np.random.choice(n_samples, size=subsample_size, replace=replacements)

        X_subset = X[indices].tolist()
        y_subset = y[indices].tolist()

        subsets.append((X_subset, y_subset))

    return subsets
