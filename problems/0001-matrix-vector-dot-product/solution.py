def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	if not a:
		return []

	num_cols = len(a[0])

	# check if the number of col in a matches len of b
	if len(b) != num_cols or any(len(row) != num_cols for row in a):
		return -1

	# dot product for each row with vector b
	return [sum(r_val * b_val for r_val, b_val in zip(row, b)) for row in a]
