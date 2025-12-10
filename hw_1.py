import networkx as nx
import matplotlib.pyplot as plt

# Завдання 1

graph = {
    'K': ['A'],
    'E': ['A'],
    'F': ['B'],
    'R': ['B'],
    'A': ['B', 'C'],
    'B': ['A', 'C'],
}

G = nx.Graph(graph)

num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()

print(f'Kількість вершин: {num_nodes}')
print(f'Kількість ребер: {num_edges}')
print(f'Ступінь вершин:{dict(G.degree())}')


nx.draw(G, with_labels=True)
plt.show()
