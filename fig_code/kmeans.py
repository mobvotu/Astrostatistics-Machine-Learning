import matplotlib.pyplot as plt
from sklearn.datasets.samples_generator import make_blobs
from sklearn.cluster import KMeans



def plot_kmeans():
    X, y = make_blobs(n_samples=300, centers=4,
                      r