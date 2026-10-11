import numpy as np

def accuracy_score(y_true, y_pred):
	# Your code here
	y_true = np.array(y_true)
	y_pred = np.array(y_pred)

	if y_true.size == 0:
		return 0.0

	correct = np.sum(y_true == y_pred)
	total = y_true.size

	return float(correct / total)
