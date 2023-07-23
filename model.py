import numpy as np

class KMeans:
    def __init__(self, k: int, epsilon: float = 1e-6) -> None:
        self.num_clusters = k
        self.cluster_centers = None
        self.epsilon = epsilon
    
    def fit(self, X: np.ndarray, max_iter: int = 150) -> None:
        # Initialize cluster centers (need to be careful with the initialization,
        # otherwise you might see that none of the pixels are assigned to some
        # of the clusters, which will result in a division by zero error)
        indices = np.random.choice(X.shape[0], self.num_clusters, replace=False)

        self.cluster_centers = X[indices]
        old_cluster_centers = np.zeros((self.num_clusters, X.shape[1]))
        for i in range(max_iter):
            # Assign each sample to the closest prototype
            cluster_indices = self.predict(X)

            # Update prototypes
            for j in range(self.num_clusters):
                # print(X[cluster_indices == j].shape)
                temp = X[cluster_indices == j]
                if temp.shape[0]>0:
                    self.cluster_centers[j] = np.mean(temp, axis=0)
                else:
                    index = np.random.choice(X.shape[0],1,replace=False)
                    while index in indices:
                        index = np.random.choice(X.shape[0],1,replace=False)
                    indices = np.append(indices,index)
                    self.cluster_centers[j] = X[index]
            
            # Check if the cluster centers have converged
            if np.allclose(self.cluster_centers, old_cluster_centers, rtol=0, atol=self.epsilon):
                break

            # Update old_cluster_centers to new claculated cluster centers 
            old_cluster_centers = np.copy(self.cluster_centers)

    
    def predict(self, X: np.ndarray) -> np.ndarray:
        # Predicts the index of the closest cluster center for each data point
        distances = np.sqrt(((X - self.cluster_centers[:, np.newaxis])**2).sum(axis=2))
        return np.argmin(distances, axis=0)
    
    def fit_predict(self, X: np.ndarray, max_iter: int = 100) -> np.ndarray:
        self.fit(X, max_iter)
        return self.predict(X)
    
    def replace_with_cluster_centers(self, X: np.ndarray) -> np.ndarray:
        # Returns an ndarray of the same shape as X
        # Each row of the output is the cluster center closest to the corresponding row in X
        distances = np.sqrt(((X - self.cluster_centers[:, np.newaxis])**2).sum(axis=2))
        return self.cluster_centers[np.argmin(distances, axis=0)]
