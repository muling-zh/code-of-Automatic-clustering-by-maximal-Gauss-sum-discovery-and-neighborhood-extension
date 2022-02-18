"""
@author  Miaolong Ye (yemiao.long@qq.com),Chengbao Zhou (z781849955@163.com) and Bo Li (kingrayli@163.com).
@desc    Code for the paper "Automatic clustering by maximal Gauss sum discovery and neighborhood extension"
@date    2022/01/18
@license GPL
"""

import matplotlib.pyplot as plt
import scipy.signal as signal
import numpy as np

from getColors import ncolors


def show_final_result(cluster, norm_data, chose_list, filepath=None):
    """
    Display the final clustering results (2D).

    :param cluster:    label list of clustering results
    :param norm_data:  raw data of location
    :param chose_list: selected peak point set
    :param filepath:   filepath of dataset
    :return:           none
    """
    colors = np.array(ncolors(len(chose_list)))
    cluster = np.array(cluster)
    empty = np.argwhere(cluster == -1)
    plt.figure(figsize=(10, 10), dpi=300)
    plt.title('The Result Of Cluster')
    plt.scatter(x=norm_data[:, 0], y=norm_data[:, 1], c=colors[cluster], s=20, marker='o', alpha=0.66)
    plt.scatter(x=norm_data[chose_list, 0], y=norm_data[chose_list, 1], marker='*', s=100, c='k', alpha=0.8)
    if len(empty) != 0:
        plt.scatter(x=norm_data[empty, 0], y=norm_data[empty, 1], c='k', s=10, marker='o', alpha=0.66)
    if filepath:
        plt.savefig(filepath)
    plt.show()


def show_nodes_for_leaders(distance, density, leader_index, leaders_list, Order):
    """
    Draw the distance density space and find the local peak point.

    :param distance:     distance matrix of dataset
    :param density:      density list
    :param leader_index: the index of current leader
    :param leaders_list: the list of all leader
    :param Order:        parameters for finding peaks
    :return:             none
    """
    sort_distance = np.sort(distance[leader_index])
    argsort_distance = np.argsort(distance[leader_index])
    sort_density = density[argsort_distance]
    arg_rel = np.array(
        signal.argrelextrema(
            sort_density, np.greater_equal,
            order=int(len(distance[leader_index]) * Order)
        )
    )[0]

    # draw
    plt.figure(figsize=(10, 9))
    plt.scatter(x=sort_distance, y=sort_density, c='k', marker='o')
    plt.scatter(x=sort_distance[arg_rel], y=sort_density[arg_rel], c='r', marker='o')
    plt.scatter(x=sort_distance[0], y=sort_density[0], c='r', marker='o')
    plt.xlim(0)
    plt.ylim(0)
    plt.xlabel('distance')
    plt.ylabel('density')
    plt.title('distance-density space')
    plt.show()

    new_leaders = list(np.argsort(distance[leader_index])[arg_rel])
    if leader_index not in new_leaders:
        new_leaders.insert(0, leader_index)

    print("Current leaders = ", new_leaders)
    print("Density of leaders = ", density[new_leaders])
    print()

    for index in range(len(new_leaders)):
        if new_leaders[index] not in leaders_list:
            leaders_list.append(new_leaders[index])
            show_nodes_for_leaders(distance, density, new_leaders[index], leaders_list, Order)
