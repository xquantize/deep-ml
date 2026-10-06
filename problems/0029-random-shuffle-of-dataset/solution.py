import numpy as np

def shuffle_data(X, y, seed=None):
	X_arr = np.array(X)
	y_arr = np.array(y)

	if seed is not None:
		np.random.seed(seed)

	indices = np.random.permutation(len(X_arr))

	return X_arr[indices], y_arr[indices]
