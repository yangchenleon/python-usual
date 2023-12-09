from os import closerange
from turtle import color
import numpy as np
from matplotlib import pyplot as plt

def read_net(filename):
    # return {node1:[n2,n3], node2:[n4,n6], ...}
    lines = list()
    net = dict()
    with open(filename) as file:
        lines = file.readlines()
        
    for line in lines:
        if line[0] == '#':
            continue
        st, ed = line.split()
        if st not in net:
            net[st] = [ed]
        else:
            net[st] += [ed]
    return net

def count_degree(net):
    # return {degree1:cntfrac1, degree2:cntfrac2, ...}
    node_cnt = dict()
    for neighbors in net.values():
        degree = len(neighbors)
        if degree not in node_cnt:
            node_cnt[degree] = 1
        else:
            node_cnt[degree] += 1
    num_node = len(net.keys())
    for degree in node_cnt.keys():
        node_cnt[degree] /= num_node
    return node_cnt


if __name__ == "__main__":
    net_file = "./degree-distribution/web-Stanford.txt"
    net = read_net(net_file)
    degree_cnt = count_degree(net)
    degree_cnt = sorted(degree_cnt.items(), key=lambda x:x[0])
    x, y = zip(*degree_cnt)
    x, y = np.array(x), np.array(y)
    plt.plot(x, y, color='b')
    
    x2 = np.array(range(1, max(x)), dtype=np.float32)
    y2 = np.power(x2, -1.1) * 0.16
    plt.plot(x2, y2, linestyle='--', color='y')

    plt.legend(["Stanford graph", "power-law"], loc='upper left')
    plt.xlabel("node degree $d$")
    plt.ylabel("the fraction of user on degree $p_d$")
    plt.title("Web graph degree distribution from Stanford")

    plt.show()