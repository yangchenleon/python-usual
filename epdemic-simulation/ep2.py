import networkx as nx
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
# 确保 中文 和 -
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def update_node_status(G, node, beta, gamma):
    """
    更改节点状态
    :param G: 输入图
    :param node: 节点序数
    :param beta: 感染率
    :param gamma: 免疫率
    """
    # 如果当前节点状态为 感染者(I) 有概率gamma变为 免疫者(R)
    if G.nodes[node]['status'] == 'I':
        p = random.random()
        if p < gamma:
            G.nodes[node]['status'] = 'R'
    # 如果当前节点状态为 易感染者(S) 有概率beta变为 感染者(I)
    if G.nodes[node]['status'] == 'S':
        for adj_node in G[node]:
            if G.nodes[adj_node]['status'] == 'I':
                p = random.random()
                if p < beta:
                    G.nodes[node]['status'] = 'I'
                    break


def update_network_data(G, beta, gamma):
    """
    更改图数据
    :param G: 输入图
    :param beta: 感染率
    :param gamma: 免疫率
    """
    for node in G:
        update_node_status(G, node, beta, gamma)


def initial_network_data(G, i_num, r_num):
    """
    初始化图数据
    :param G: 输入图
    :param i_num: 感染者数量
    :param r_num: 免疫者数量
    """
    # 感染节点集
    i_set = set(random.sample(G.nodes, i_num))
    # 免疫节点集
    r_set = set(random.sample(G.nodes, r_num))
    # 两个集合不能重复
    while r_set & i_set:
        r_set = set(random.sample(G.nodes, r_num))
    # 初始化节点状态
    for node in G:
        if node in i_set:
            G.nodes[node]['status'] = 'I'
        elif node in r_set:
            G.nodes[node]['status'] = 'R'
        else:
            G.nodes[node]['status'] = 'S'


def count_node(G):
    """
    计算当前图内各个节点的数目
    :param G: 输入图
    :return: 各个节点数目
    """
    s_num, i_num, r_num = 0, 0, 0
    for node in G:
        if G.nodes[node]['status'] == 'S':
            s_num += 1
        elif G.nodes[node]['status'] == 'I':
            i_num += 1
        else:
            r_num += 1
    return s_num, i_num, r_num


def draw_network(G):
    """
    输出初始网络节点分布
    :param G: 输入图
    """
    # 设置图大小
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_title("易感染者-感染者-免疫者节点初始分布")
    pos = nx.spring_layout(G, scale=1)
    nx.draw(G, pos=pos, with_labels=True, font_color='white', edge_color='grey',
            node_color=[color_dict[ba.nodes[node]['status']] for node in G])


def draw_node_trend(G, beta, gamma):
    """
    输出各类节点趋势
    :param G: 输入图
    :param beta: 感染率
    :param gamma: 免疫率
    """
    # 设定传播步长
    t_list = np.linspace(1, 24, 24)
    # 开始模拟传播
    for t in range(len(t_list)):
        # 计算并存储当前各个节点数目
        node_list.append(count_node(G))
        update_network_data(G, beta, gamma)
    # 整理数据
    df = pd.DataFrame(data=node_list, index=t_list, columns=['S', 'I', 'R'])
    # 显示数据曲线
    df.plot(figsize=(8, 6), color=[color_dict.get(x) for x in df.columns])
    plt.ylabel('nodes(节点数)')
    plt.xlabel('days(天数)')
    plt.title('易感染者-感染者-免疫者节点趋势')
    plt.savefig('SIR_model')
    plt.show()


def update_graph(i, G, ax, pos, beta, gamma):
    """
    动态更新节点
    :param i: 输入帧
    :param ax: 输入图参数
    :param G: 输入图
    :param beta: 感染率
    :param gamma: 免疫率
    """
    i = int(i)
    ax.set_title("第" + str(i + 1) + "天 易感染者-感染者-免疫者节点分布")
    ax.axis('off')
    plt.box(False)
    if i == 1:
        # 第一天  初始节点分布  直接画出
        nx.draw(G, with_labels=True, font_color='white', edge_color='grey',
                node_color=[color_dict[ba.nodes[node]['status']] for node in G], pos=pos)
    else:
        # 以后变化 需要演变节点
        update_network_data(G, beta, gamma)
        nx.draw_networkx_nodes(G, with_labels=True, font_color='white', edge_color='grey',
                               node_color=[color_dict[ba.nodes[node]['status']] for node in G], pos=pos)


def draw_network_trend(G, beta, gamma, days):
    """
    输出网络动态变化视频
    :param G: 输入图
    :param beta: 感染率
    :param gamma: 免疫率
    :param days: 需要的时间(迭代次数)
    """
    fig, ax = plt.subplots(figsize=(12, 8))
    pos = nx.spring_layout(G, scale=1)
    ani = animation.FuncAnimation(fig, update_graph, frames=days,
                                  fargs=(G, ax, pos, beta, gamma), interval=300)
    writer = animation.FFMpegWriter()
    ani.save('network_trend.mp4', writer=writer)


if __name__ == '__main__':
    # 总人数
    N = 10000
    # 易感染者人数
    s = 9980
    # 感染者人数
    i = 18
    # 免疫者人数
    r = N - s - i
    # 各个节点数目列表
    node_list = []
    # 节点颜色
    color_dict = {'S': 'blue', 'I': 'red', 'R': 'green'}
    # 创建BA无标度网络
    ba = nx.barabasi_albert_graph(N, 3, seed=1)
    # 初始化网络节点
    initial_network_data(ba, i, r)
    # 输出节点趋势图
    draw_node_trend(ba, 0.4, 0.1)
    # 初始节点分布图
    # 输出初始节点网络图
    draw_network(ba)
    # 输出网络动态变化图
    draw_network_trend(ba, 0.2, 0.15, 50)
