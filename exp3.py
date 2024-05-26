import networkx as nx
import matplotlib.pyplot as plt

# 展示网络图
def plot_network(G, activated_nodes, title):
    node_labels = {node: f"{node}\n{data['weight']}" for node, data in G.nodes(data=True)}
    edge_labels = {(u, v): f"{data['weight']}" for u, v, data in G.edges(data=True)}
    node_colors = ['red' if node in activated_nodes else 'skyblue' for node in G.nodes()]
    pos = nx.spring_layout(G, seed=818) 
    plt.figure(figsize=(6, 6))
    nx.draw(G, pos, with_labels=True, labels=node_labels, node_size=700, node_color=node_colors, arrowsize=20, font_size=15)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12, label_pos=0.3)
    manager = plt.get_current_fig_manager()
    manager.window.wm_title(title)
    plt.show()

def linear_threshold_model(G, start):
    # Activated nodes
    activated = set(start)
    newly_activated = set(start)
    activation_history = [set(start)]
    node_labels = {node: data for node, data in G.nodes(data=True)}
    edge_labels = {(u, v): f"{data['weight']}" for u, v, data in G.edges(data=True)}
    i = 0
    while newly_activated:
        current_activated = set()
        for node in G.nodes():
            if node not in activated:
                s = 0
                for neighbor in G.nodes():
                    if node in G.neighbors(neighbor) and neighbor in activated:
                        s += G[neighbor][node]['weight']
                if s >= node_labels[node]['weight']:
                    current_activated.add(node)
        
        newly_activated = current_activated
        if newly_activated:
            activated.update(newly_activated)
            activation_history.append(newly_activated)
            i += 1
            plot_network(G, activated, f"第{i}次传播")
    return activation_history

if __name__ == "__main__":
    # 创建一个有向图
    G = nx.DiGraph()

    # 添加节点
    nodes = [(1, {'weight': 0.6}), (2, {'weight': 0.5}), (3, {'weight': 0.7}), (4, {'weight': 0.9})]
    G.add_nodes_from(nodes)
    # 添加有向边并赋值属性
    edges = [(1, 2, {'weight': 0.5}),
             (1, 3, {'weight': 0.5}),
             (2, 3, {'weight': 0.5}),
             (3, 2, {'weight': 0.5}),
             (2, 4, {'weight': 0.5}),
             (3, 4, {'weight': 0.5}),
            ]

    G.add_edges_from(edges)
    plot_network(G, [1], '初始状态')
    print([j for j in G.neighbors(1)])
    linear_threshold_model(G, [1])
