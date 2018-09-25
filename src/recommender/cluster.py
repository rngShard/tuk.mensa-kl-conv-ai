import pickle

import graphviz
import numpy as np
from sklearn import tree
from sklearn.cluster import KMeans

from definitions import ROOT_DIR
from util.cloud_connection import bucket_connection


class Cluster:

    def __init__(self):
        Cluster.download_cluster_data()
        self.load_cluster_data()

    def load_cluster_data(self):
        path = ROOT_DIR + "/.cluster_data/"
        self.kmeans = pickle.load(open(path + "kmeans.pkl", "rb"))
        self.cluster_labels = pickle.load(open(path + "cluster_labels.pkl", "rb"))
        self.clusters = pickle.load(open(path + "clusters.pkl", "rb"))
        self.dTree = pickle.load(open(path + "dTree.pkl", "rb"))
        self.decision_points = pickle.load(open(path + "decision_points.pkl", "rb"))

    @staticmethod
    def download_cluster_data():
        path = ROOT_DIR + "/.cluster_data/"
        bucket_connection.download_blob("conv_ai_cluster_data", "kmeans.pkl", path + "kmeans.pkl")
        bucket_connection.download_blob("conv_ai_cluster_data", "cluster_labels.pkl",
                                        path + "cluster_labels.pkl")
        bucket_connection.download_blob("conv_ai_cluster_data", "clusters.pkl", path + "clusters.pkl")
        bucket_connection.download_blob("conv_ai_cluster_data", "dTree.pkl", path + "dTree.pkl")
        bucket_connection.download_blob("conv_ai_cluster_data", "decision_points.pkl",
                                        path + "decision_points.pkl")

    @staticmethod
    def create_initial_clusters(df_user_similarity, n_clusters):
        kmeans = KMeans(n_clusters=n_clusters)
        cluster_labels = kmeans.fit_predict(df_user_similarity)
        pickle.dump(kmeans, open("initial_cluster.pkl", "wb"))

        clusters = []
        for cl in set(cluster_labels):
            cluster = list(np.where(cluster_labels == cl)[0])
            cluster = [i + 1 for i in cluster]
            clusters.append(cluster)

        return clusters, cluster_labels

    def get_clusters(self):
        return self.clusters

    def get_cluster_labels(self):
        return self.cluster_labels

    def get_neighbbors(self, current_cluster):
        return self.clusters[current_cluster]

    def get_decision_points(self):
        return self.decision_points

    @staticmethod
    def create_decision_tree(df_user_item, cluster_labels):
        dTree = tree.DecisionTreeClassifier(max_leaf_nodes=5)
        dTree.fit(df_user_item, cluster_labels)
        pickle.dump(dTree, open("initial_decision_tree.pkl", "wb"))

        dot_data = tree.export_graphviz(dTree, out_file=None)
        graph = graphviz.Source(dot_data)
        graph.render("decisionTree")

        return dTree, dot_data

    def predict_cluster(self, user_ratings):
        return self.dTree.predict(np.array(user_ratings).reshape(1, -1))


if __name__ == "__main__":
    Cluster.download_cluster_data()
    cluster = Cluster()
    print(cluster.get_decision_points())
    test_user1 = np.zeros(cluster.dTree.n_features_)
    test_user1[75] = 2
    print(cluster.predict_cluster(test_user1))
