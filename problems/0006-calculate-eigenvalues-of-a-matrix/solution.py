import math
import cmath

def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	a, b = matrix[0]
	c, d = matrix[1]
	trace = a + d
	det = a * d - b * c
	discriminant = trace ** 2 - 4 * det

	if discriminant >= 0:
		root = math.sqrt(discriminant)
	else:
		root = cmath.sqrt(discriminant)

	eigenvalues = [(trace + root) / 2, (trace - root) / 2]

	return sorted(eigenvalues, key=lambda v: v.real, reverse=True)
