import networkx as nx
import matplotlib.pyplot as plt

# 生成小世界网络
n = 20  # 节点数量
k = 4   # 每个节点的邻居数
p = 0.3 # 重连概率
graph = nx.watts_strogatz_graph(n, k, p)

# 绘制图形
pos = nx.spring_layout(graph)
nx.draw(graph, pos, with_labels=True, node_color='lightblue', edge_color='gray')
plt.title('Small-World Network')
plt.show()

# 分析图的性质
average_shortest_path = nx.average_shortest_path_length(graph)
print("Average Shortest Path Length: ", average_shortest_path)

average_clustering = nx.average_clustering(graph)
print("Average Clustering Coefficient: ", average_clustering)
