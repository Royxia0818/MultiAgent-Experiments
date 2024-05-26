# 实验选题1.1-1.4
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

# 展示网络图
def plot_network(G, title):
    pos = nx.spring_layout(G)
    plt.figure(figsize=(6, 6))
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=700, edge_color='gray') 
    manager = plt.get_current_fig_manager()
    manager.window.wm_title(title)
    plt.show()

def create_nearest_neighbor_coupled_network(n, k):
    """
    创建一个最近邻耦合网络，其中每个节点连接到其k个最近的邻居。
    
    参数:
    n - 节点数
    k - 每个节点连接的最近邻居数（必须是偶数）
    
    返回:
    G - 最近邻耦合网络
    """
    if k % 2 != 0:
        raise ValueError("k must be even")
    G = nx.cycle_graph(n)  # 创建一个包含n个节点的环状网络
    # 为每个节点添加k/2个最近邻居的边
    for i in range(1, k//2 + 1):
        edges_to_add = [(j, (j + i) % n) for j in range(n)]
        G.add_edges_from(edges_to_add)
    return G

# 主程序
if __name__ == "__main__":
    print("全局耦合网络")
    G = nx.complete_graph(10) # 创建一个包含10个节点的全局耦合网络
    print(f"平均路径长度: {nx.average_shortest_path_length(G)}")
    print(f"聚类系数: {nx.average_clustering(G)}")
    plot_network(G, title="全局耦合网络")

    print("最近邻耦合网络") # 创建一个包含20个节点的最近邻耦合网络，k=4
    G = create_nearest_neighbor_coupled_network(20, 4)
    print(f"平均路径长度: {nx.average_shortest_path_length(G)}")
    print(f"聚类系数: {nx.average_clustering(G)}")
    plot_network(G, title="最近邻耦合网络")

    print("星形网络")
    G = nx.star_graph(9) # 创建一个包含10个节点的星形网络
    print(f"平均路径长度: {nx.average_shortest_path_length(G)}")
    print(f"聚类系数: {nx.average_clustering(G)}")
    plot_network(G, title="星形网络")

    print("随机网络")
    G = nx.erdos_renyi_graph(10, 0.3)
    print(f"平均路径长度: {nx.average_shortest_path_length(G)}")
    print(f"聚类系数: {nx.average_clustering(G)}")
    plot_network(G, title="随机网络")

