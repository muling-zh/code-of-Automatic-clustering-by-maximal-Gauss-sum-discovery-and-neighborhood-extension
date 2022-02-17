import numpy as np
from numba import jit


@jit
def euclideanDistance(v):
    """
    Calculate the Euclidean distance between any two points and return it as a matrix.

    :param v: data list
    :return:  distance matrix
    """
    distance = np.zeros(shape=(len(v), len(v)))
    for i in range(len(v)):
        for j in range(len(v)):
            if i > j:
                distance[i][j] = distance[j][i]
            elif i < j:
                distance[i][j] = np.sqrt(np.sum(np.power(v[i] - v[j], 2)))
    return distance

#
@jit
def cosineDistance(v):
    """
    Calculate the cosine similarity between any two points.

    :param v: data list
    :return:  distance matrix
    """
    distance = np.zeros(shape=(len(v), len(v)))
    for i in range(len(v)):
        for j in range(len(v)):
            if i > j:
                distance[i][j] = distance[j][i]
            elif i < j:
                distance[i][j] = (np.sum(v[i] * v[j])) / \
                                 (np.sqrt(np.sum(np.power(v[i], 2))) *
                                  np.sqrt(np.sum(np.power(v[j], 2))))
            else:
                distance[i][j] = 1
    distance = 1 - distance
    return distance
