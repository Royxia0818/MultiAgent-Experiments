# 实验一

## 实验要求

1. 实现全局耦合网络，展示网络图，并计算平均路径长度和聚类系数。

2. 实现最近邻耦合网络，展示网络图，并计算平均路径长度和聚类系数。

3. 实现星形网络，展示网络图，并计算平均路径长度和聚类系数。

4. 实现随机网络，展示网络图，并计算平均路径长度和聚类系数。

## 全局耦合网络

在一个全局耦合网络中，每个节点与网络中的所有其他节点都直接相连。我们使用networkx创建了一个包含10个节点的全局耦合网络。代码如下：

```python
print("全局耦合网络")
    G = nx.complete_graph(10) # 创建一个包含10个节点的全局耦合网络
    print(f"平均路径长度: {nx.average_shortest_path_length(G)}")
    print(f"聚类系数: {nx.average_clustering(G)}")
    plot_network(G, title="全局耦合网络")
```

得到全局耦合网络的平均路径长度为1.0， 聚类系数为1.0。绘制全局耦合网络图如下：

![全局耦合网络](figure/全局耦合网络.png)

## 最近邻耦合网络

在一个最近邻耦合网络中，每个节点仅与k个最近邻节点相连，通常以环形连接。最近邻耦合网络的创建可以基于一个环形网络。首先创建一个包含20个节点的最近邻耦合网络，然后将每个节点与其相邻的4个节点相连，便完成了最近邻耦合网络的创建。在创建时，需要注意k必须是偶数，否则主动产生报错来提高程序鲁棒性。代码如下：

```python
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

print("最近邻耦合网络") # 创建一个包含20个节点的最近邻耦合网络，k=4
G = create_nearest_neighbor_coupled_network(20, 4)
print(f"平均路径长度: {nx.average_shortest_path_length(G)}")
print(f"聚类系数: {nx.average_clustering(G)}")
plot_network(G, title="最近邻耦合网络")
```

得到最近邻耦合网络的平均路径长度为1.895， 聚类系数为0.5。绘制最近邻耦合网络的图片如下：

![最近邻耦合网络](figure/最近邻耦合网络.png)

## 星形网络

在星形网络中，一个中心节点与所有其他节点直接相连，而其他节点之间没有连接。我们使用networkx创建了一个包含10个节点的星形网络。代码如下：

```python
print("星形网络")
    G = nx.star_graph(9) # 创建一个包含10个节点的星形网络
    print(f"平均路径长度: {nx.average_shortest_path_length(G)}")
    print(f"聚类系数: {nx.average_clustering(G)}")
    plot_network(G, title="星形网络")
```

得到星形网络的平均路径长度为1.8， 聚类系数为0.0。绘制星形网络的图片如下：

![星形网络](figure/星形网络.png)

## 随机网络

在一个ER随机网络中，网络中的每一对节点以固定概率随机连接。我们使用networkx创建了一个包含10个节点的随机网络，其中每一对节点以0.3的概率连接。代码如下：

```python
print("随机网络")
    G = nx.erdos_renyi_graph(10, 0.3)
    print(f"平均路径长度: {nx.average_shortest_path_length(G)}")
    print(f"聚类系数: {nx.average_clustering(G)}")
    plot_network(G, title="随机网络")
```

得到随机网络的平均路径长度为1.956， 聚类系数为0.227。绘制随机网络的图片如下：

![随机网络](figure/随机网络.png)

## 总结
|名称|平均路径长度|聚类系数|
|:---:|:---:|:---:|
|全连接网络|1.0|1.0|
|最近邻耦合网络|2.895|0.5|
|星形网络|1.8|0.0|
|随机网络|1.956|0.227|

对上述数据进行可视化，可以得到：

![实验一结果](figure/实验一表格.png)

# 实验二