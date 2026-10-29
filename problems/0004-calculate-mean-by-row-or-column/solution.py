def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	if mode == 'row':
		means = [sum(row) / len(row) for row in matrix]
	elif mode == 'column':
		means = [sum(col) / len(col) for col in zip(*matrix)]
	else:
		raise ValueError("mode must be row or column")

	return means
