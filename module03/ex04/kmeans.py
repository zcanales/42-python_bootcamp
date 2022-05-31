from csvreader import CsvReader
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class KmeansClustering:
    def __init__(self, max_iter=20, ncentroid=5):
        self.ncentroid = ncentroid #number of centroids
        self.max_iter = max_iter #number of max iterations to update the centroids
        self.centroids = [] # values of the centroids
    def fit(self, X):
        """
        Run the K-means clustering algorithm
        For the location of the initial centroids, random pick ncentroids from the dataset.
        Args:
            X: has to be an numpy.ndarray, a matrice of dimention m * n.
        Returns:
            None.
        Raises.
            This funciton shluods not raise any Exception.
        """
        n_entries = X.shape[0]
        n_data = X.shape[1] - 1
        self.centroids = [X[i] for i in random.sample(range(n_entries), self.ncentroid)]
        belonging = [-1] * n_entries
        # for _i in range(self.max_iter):
        print(self.centroids)
        for entry in X:
            distances = [self.get_dist(X, centroid[0], entry[0]) for centroid in self.centroids]
            belonging[entry[0]] = distances.index(min(distances))
        print(belonging)
        for centroid in range(self.ncentroid):
            for data in range(1, n_data):
                self.centroids[centroid][data] = self.get_mean(X, belonging, centroid, data)
        print(self.centroids)
        pass
    def predit(self, X):
        """
        Predict from which cluster each datapoint belongs to.
        Args:
            X: has to be an numpy.ndarray, a matrice of dimention m * n.
        Returns:
            The prediction has a numpy.ndarra, a vextor of dimension m * n.
        Raises.
            This funciton shluods not raise any Exception.
        """

if __name__ == "__main__":
    k = KmeansClustering()
    data = pd.read_csv('solar_system_census.csv')
    print(data)
    plt.scatter(data['height'],data['weight'])
    plt.xlim(0,300)
    plt.ylim(0,300)
    plt.show()
    x = data.iloc[:,1:3] # 1t for rows and second for columns
    print(x)
    #k.fit(data.astype(np.float))