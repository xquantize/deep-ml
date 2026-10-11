import numpy as np

def divide_on_feature(X, feature_i, threshold):
	# Your code here
	X = np.array(X)

	if isinstance(threshold, (int, float)):
		mask = X[:, feature_i] >= threshold
	else:
		mask = X[:, feature_i] == threshold

	X_1 = X[mask]
	X_2 = X[~mask]

	return [X_1, X_2]
