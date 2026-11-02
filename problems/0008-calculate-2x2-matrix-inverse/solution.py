def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    """
    Calculate the inverse of a 2x2 matrix.
    
    Args:
        matrix: A 2x2 matrix represented as [[a, b], [c, d]]
    
    Returns:
        The inverse matrix as a 2x2 list, or None if the matrix is singular
        (i.e., determinant equals zero)
    """
    if len(matrix) != 2 or len(matrix[0]) != 2 or len(matrix[1]) != 2:
        return None
        
    a, b = matrix[0]
    c, d = matrix[1]
    
    det = a * d - b * c
    
    if det == 0:
        return None
        
    inv_matrix = [
        [d / det, -b / det],
        [-c / det, a / det]
    ]
    
    return inv_matrix
