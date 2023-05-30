import networkx as nx
import matplotlib.pyplot as plt

# 生成 Erdős-Rényi 随机图
n = 20  # 节点数量
p = 0.3  # 任意两个节点之间存在边的概率
graph = nx.erdos_renyi_graph(n, p)

# 绘制图形
pos = nx.spring_layout(graph)
nx.draw(graph, pos, with_labels=True, node_color='lightblue', edge_color='gray')
plt.title('Erdős-Rényi Random Graph')
plt.show()

# 分析图的性质
average_degree = sum(dict(graph.degree()).values()) / n
print("Average Degree: ", average_degree)

average_clustering = nx.average_clustering(graph)
print("Average Clustering Coefficient: ", average_clustering)

