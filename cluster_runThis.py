"""
@author  Miaolong Ye (yemiao.long@qq.com),Chengbao Zhou (z781849955@163.com) and Bo Li (kingrayli@163.com).
@desc    Code for the paper "Automatic clustering by maximal Gauss sum discovery and neighborhood extension"
@date    2022/01/18
@license GPL
"""

import numpy as np
import collections
import copy

from distance_calculation import euclideanDistance, cosineDistance
from eval import accuracy
from show import show_nodes_for_leaders, show_final_result


def chose_dc(disMat, p):
    """
    Obtain DC.
    The value of p means that the nearest points around each point are t%
    of the total points.Select DC according to the given p.The input of p
    is the integer part of the percentage.For example, 2% only needs to be
    input chose_dc(disMat, 2).

    :param disMat: distance matrix of dataset
    :param p:      percent in sorted distance list
    :return dc:    the value of dc
    """
    temp = []
    for i in range(len(disMat[0])):
        for j in range(i + 1, len(disMat[0])):
            temp.append(disMat[i][j])
    temp.sort()
    dc = temp[int(len(temp) * p / 100) - 1]
    return dc


def count_density(distance, dc):
    """
    Measure the density of a point by counting the number of points whose
    distance is less than DC (discrete type).

    :param distance: distance matrix of dataset
    :param dc:       dc in paper
    :return density: density list by cut kernel
    """
    density = np.zeros(shape=len(distance))
    for index, node in enumerate(distance):
        density[index] = len(node[node < dc])
    return density


def gauss_density(distance, dc):
    """
    By the Gauss formula {np.sum(np.exp(-(node / dc) ** 2))} measures the
    density of a store (continuous type).

    :param distance: distance matrix of dataset
    :param dc:       dc in paper
    :return density: density list by points Gauss kernel
    """
    density = np.zeros(shape=len(distance))
    for index, node in enumerate(distance):
        density[index] = np.sum(np.exp(-(node / dc) ** 2))
    max_density = np.squeeze(np.argwhere(density == np.max(density)))
    if max_density.size > 1:
        density[max_density[0]] *= 1.01
    return density


def final_clustering(distance, density, centroid, eps):
    """
    Clustering process in paper.

    :param distance: distance matrix of dataset
    :param density:  density list of dataset
    :param centroid: the index of leaders
    :param eps:      the radius choiced by P0
    :return cluster: label list of data
    """
    k = -1
    neighbor_list = []                              # the neighborhood used to store each data
    gama = set([x for x in range(len(distance))])   # initially mark all points as not accessed
    cluster = -np.ones(len(distance), dtype=int)    # cluster result marked -1
    for i in range(len(distance)):
        neighbor_list.append(set(np.argwhere(distance[i] <= eps).reshape(-1)))
    center = np.array(centroid)[np.argsort(density[centroid])]
    for j in center:
        if j in gama:
            gama_old = copy.deepcopy(gama)
            k = k + 1
            Q = list(neighbor_list[j])
            Q.insert(0, j)
            Q = np.array(Q)[np.argsort(density[Q])]
            total_Q = copy.deepcopy(Q)
            gama = gama - set(Q)
            while len(Q) > 0:
                q = Q[0]
                Q = np.delete(Q, 0)
                if len(neighbor_list[q] & set(total_Q)) > 2 and neighbor_list[q] & gama:
                    delta = neighbor_list[q] & gama
                    delta_sort = np.array(list(delta))[np.argsort(density[list(delta)])]
                    Q = np.append(Q, delta_sort)
                    total_Q = np.append(total_Q, delta_sort)
                    gama = gama - delta
            Ck = gama_old - gama
            Cklist = list(Ck)
            for i in Cklist:
                cluster[i] = k
    return cluster


def main(input_x):
    """
    Entry function.

    :param input_x: data load by numpy array
    :return:        none
    """
    norm_data = input_x
    distance = euclideanDistance(norm_data)     # euclidean distance matrix between sample points
    # distance = cosineDistance(norm_data)      # cosine similarity matrix
    dc = chose_dc(distance, Dc_per)             # select the appropriate dc according to t
    eps = np.power(-np.log(P0), 1 / 2) * dc
    density = gauss_density(distance, dc)       # calculate the Gaussian density of sample points
    # density = count_density(distance, dc)     # or calculate the point density value of sample points
    print("dc =", dc)
    print("eps =", eps)
    print()

    max_density = np.argmax(density)
    leaders_list = [max_density]                # list of initial density peak points

    show_nodes_for_leaders(                     # draw the distance density space and find out
        distance, density, max_density,         # the local peak point
        leaders_list, Order)

    cluster = final_clustering(distance, density, leaders_list, eps)  # final clustering results

    print("My leaders:", leaders_list)
    print('total:', len(norm_data))
    print('assignment:', len(cluster[cluster != -1]))
    print('assignment rate:', len(cluster[cluster != -1]) / len(norm_data))
    print(collections.Counter(cluster))
    if norm_data.shape[1] == 2:
        show_final_result(cluster, norm_data, leaders_list)
    if label['label']:
        accuracy(label['label_path'], cluster, location=label['label_location'],
                 label_string=label['label_string'])
    leaders_list.clear()


if __name__ == '__main__':
    Dc_per = 2      # dc(%) in paper
    P0 = 0.1        # p0 in paper
    Order = 0.08    # parameters for finding peaks

    data_path = 'DATA/Zigzag.txt'   # data path
    label = {'label': False,        # does the given data have a label column?
             'label_path': data_path,
             'label_location': -1,
             'label_string': False}

    dim = np.arange(0, 2)           # select data feature dimension
    raw_data = np.loadtxt(data_path, comments='@', delimiter=',', usecols=dim)
    main(raw_data)
