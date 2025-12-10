from collections import deque
import networkx as nx
import matplotlib.pyplot as plt

# Завдання 2

graph = {
    'K': ['A'],
    'E': ['A'],
    'F': ['B'],
    'R': ['B'],
    'A': ['B', 'C', 'E', 'K'],
    'B': ['A', 'C', 'F', 'R'],
    'C': ['A', 'B']
}

G = nx.Graph(graph)


# Рекурсивна реалізація алгоритму DFS
def dfs_recursive(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    visited.add(vertex)
    print(vertex, end=' ')
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

# Рекурсивна реалізація BFS


def bfs_recursive(graph, queue, visited=None):
    # Перевіряємо, чи існує множина відвіданих вершин, якщо ні, то ініціалізуємо нову
    if visited is None:
        visited = set()
    # Якщо черга порожня, завершуємо рекурсію
    if not queue:
        return
    # Вилучаємо вершину з початку черги
    vertex = queue.popleft()
    # Перевіряємо, чи відвідували раніше дану вершину
    if vertex not in visited:
        # Якщо не відвідували, друкуємо вершину
        print(vertex, end=" ")
        # Додаємо вершину до множини відвіданих вершин.
        visited.add(vertex)
        # Додаємо невідвіданих сусідів даної вершини в кінець черги.
        queue.extend(set(graph[vertex]) - visited)
    # Рекурсивний виклик функції з тією ж чергою та множиною відвіданих вершин
    bfs_recursive(graph, queue, visited)


print('DFS:')
dfs_recursive(graph, 'K')

print('\nBFS:')
bfs_recursive(graph, deque(['K']))


nx.draw(G, with_labels=True)
plt.show()
