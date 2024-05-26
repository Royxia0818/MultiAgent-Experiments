# 实验选题2.1-2.3
import networkx as nx
import matplotlib.pyplot as plt


def plot_network(G, title):
    pos = nx.spring_layout(G)
    plt.figure(figsize=(6, 6))
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=700, edge_color='gray') 
    manager = plt.get_current_fig_manager()
    manager.window.wm_title(title)
    plt.show()


if __name__ == "__main__":
    print("WS小世界模型")
    G = nx.watts_strogatz_graph(20, 4, 0.1) # 创建一个包含20个节点的WS小世界模型
    print(f"平均路径长度: {nx.average_shortest_path_length(G)}")
    print(f"聚类系数: {nx.average_clustering(G)}")
    plot_network(G, title="WS小世界模型")
    
    print("NW小世界模型")
    G = nx.newman_watts_strogatz_graph(20, 4, 0.1) # 创建一个包含20个节点的NW小世界模型
    print(f"平均路径长度: {nx.average_shortest_path_length(G)}")
    print(f"聚类系数: {nx.average_clustering(G)}")
    plot_network(G, title="NW小世界模型")

    print("无标度网络模型")
    G = nx.barabasi_albert_graph(20, 2) # 创建一个包含20个节点的无标度世界模型
    print(f"平均路径长度: {nx.average_shortest_path_length(G)}")
    print(f"聚类系数: {nx.average_clustering(G)}")
    plot_network(G, title="无标度网络模型")
