"""
@author  xxx,xxx,xxx
@email   xxxxx@xxx.com
@desc    Code for the paper "xxxxx" (xxx 2021)
@date    2022/01/18
@license MIT
"""

import numpy as np
from sklearn import metrics
import collections


def accuracy(file_name, cluster, location, label_string):
    """
    Evaluation of clustering results (including labels).

    :param file_name:    file path of dataset
    :param cluster:      label list of cluster result
    :param location:     dimension of label
    :param label_string: label
    :return:             none
    """
    with open(file_name, 'r') as f:
        lines = f.readlines()
    labels = [l.rstrip().split(',')[location] for l in lines]
    labels_set = set(labels)
    if label_string:
        labels_to_num = {}
        for index, label in enumerate(labels_set):
            labels_to_num[label] = index
        new_labels = []
        for label in labels:
            new_labels.append(labels_to_num[label])
        new_labels = np.array(new_labels)
    else:
        new_labels = np.array(labels)
    cluster_set = set(cluster)
    if -1 in cluster_set:
        cluster_set.remove(-1)
    correct = 0
    print('cluster_set:', cluster_set)
    for i in cluster_set:
        correct += np.max(list(collections.Counter(new_labels[np.squeeze(np.argwhere(cluster == i))]).values()))
    ari_score = metrics.adjusted_rand_score(new_labels, cluster)
    ami_score = metrics.adjusted_mutual_info_score(new_labels, cluster)
    print('ARI:', ari_score)
    print('AMI:', ami_score)
    print('assignment ratio:', len(cluster[cluster != -1]) / len(cluster))
    print('assignment purity:', correct / len(cluster[cluster != -1]))
    print('purity:', correct / len(cluster))
