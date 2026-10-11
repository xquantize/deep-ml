import numpy as np
def precision(y_true, y_pred):
	# Your code here
	y_true = np.array(y_true)
	y_pred = np.array(y_pred)

	true_positives = np.sum((y_true == 1) & (y_pred == 1))
	predicted_positives = np.sum(y_pred == 1)

	if predicted_positives == 0:
		return 0.0

	return float(true_positives / predicted_positives)
