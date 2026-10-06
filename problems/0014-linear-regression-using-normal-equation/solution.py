import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	# Your code here, make sure to round
	X_arr = np.array(X, dtype=float)
	y_arr = np.array(y, dtype=float)

	theta = np.linalg.inv(X_arr.T @ X_arr) @ X_arr.T @ y_arr

	return [round(float(val), 4) for val in theta]
