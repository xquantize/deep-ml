def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
    n_features = len(vectors)
    n_obs = len(vectors[0])

    means = [sum(feature) / n_obs for feature in vectors]
    cov_matrix = [[0.0] * n_features for _ in range(n_features)]

    for i in range(n_features):
        for j in range(i, n_features):
            cov = sum(
                (vectors[i][k] - means[i]) * (vectors[j][k] - means[j])
                for k in range(n_obs)
            ) / (n_obs - 1)

            cov_matrix[i][j] = cov
            cov_matrix[j][i] = cov

    return cov_matrix
