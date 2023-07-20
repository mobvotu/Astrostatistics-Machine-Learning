import matplotlib.pyplot as plt
from sklearn.datasets.samples_generator import make_blobs
from sklearn.cluster import KMeans



def plot_kmeans():
    X, y = make_blobs(n_samples=300, centers=4,
                      random_state=0, cluster_std=0.60)

    y_pred = KMeans(4).fit(X).predict(X)

    fig, ax = plt.subplots(1, 2, figsize=(12, 6))

    ax[0].scatter(X[: