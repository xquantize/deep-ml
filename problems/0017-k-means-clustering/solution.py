def k_means_clustering(points: list[tuple[float, ...]], k: int, initial_centroids: list[tuple[float, ...]], max_iterations: int) -> list[tuple[float, ...]]:
    centroids = [list(c) for c in initial_centroids]
    dim = len(points[0]) if points else 0

    for _ in range(max_iterations):
        clusters = [[] for _ in range(k)]

        for point in points:
            min_dist = float('inf')
            closest_idx = 0

            for i, centroid in enumerate(centroids):
                dist = sum((p - c) ** 2 for p, c in zip(point, centroid))

                if dist < min_dist:
                    min_dist = dist
                    closest_idx = i

            clusters[closest_idx].append(point)

        new_centroids = []

        for i, cluster in enumerate(clusters):
            if not cluster:
                new_centroids.append(tuple(centroids[i]))
            else:
                mean_point = tuple(
                    sum(p[d] for p in cluster) / len(cluster) for d in range(dim)
                )
                new_centroids.append(mean_point)

        if new_centroids == [tuple(c) for c in centroids]:
            break

        centroids = [list(c) for c in new_centroids]

    return [tuple(c) for c in centroids]
