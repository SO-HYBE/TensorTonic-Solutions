def k_means_centroid_update(points: list, assignments: list, k: int) -> list:
    """
    Returns one updated centroid for each cluster.
    """
    # Write code here
    new_centroids = []
    for cluster in range(k):
        cluster_points = [point for i, point in enumerate(points) if cluster == assignments[i]]
        if len(cluster_points) == 0:
            new_centroids.append([0.0] * len(points[0]))
            continue
        cluster_update = []
        for i in range(len(points[0])):
            sum = 0
            for point in cluster_points:
                sum += point[i]
            mean = sum / len(cluster_points)
            cluster_update.append(mean)
        new_centroids.append(cluster_update)
        
    return new_centroids
                
        