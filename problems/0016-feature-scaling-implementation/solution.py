import numpy as np

def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
	# Your code here
	mean = np.mean(data, axis=0)
	std = np.std(data, axis=0)
	std_safe = np.where(std == 0, 1.0, std)
	standardized_data = (data - mean) / std_safe

	min_val = np.min(data, axis=0)
	max_val = np.max(data, axis=0)
	range_val = max_val - min_val
	range_safe = np.where(range_val == 0, 1.0, range_val)
	normalized_data = (data - min_val) / range_safe

	return standardized_data, normalized_data
