import numpy as np

def batch_iterator(X, y=None, batch_size=64):
	n_samples = X.shape[0]

	for i in range(0, n_samples, batch_size):
		end = min(i + batch_size, n_samples)

		if y is not None:
			yield [X[i:end].tolist(), y[i:end].tolist()]
		else:
			yield [X[i:end].tolist()]
