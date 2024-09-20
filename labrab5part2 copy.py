import matplotlib.pyplot as plt
import networkx as nx
from collections import deque

class BipartiteGraph:
    def __init__(self, adj_matrix):
        self.adj_matrix = adj_matrix
        self.n = len(adj_matrix)  # Количество вершин в левой части
        self.m = len(adj_matrix[0]) if self.n > 0 else 0  # Количество вершин в правой части
        self.pair_u = [-1] * self.n  # Пары для левой части
        self.pair_v = [-1] * self.m  # Пары для правой части
        self.dist = [-1] * self.n  # Расстояния в BFS

    def bfs(self):
        queue = deque()
        for u in range(self.n):
            if self.pair_u[u] == -1:  # Если вершина не парная
                self.dist[u] = 0
                queue.append(u)
            else:
                self.dist[u] = float('inf')

        found_augmenting_path = False
        while queue:
            u = queue.popleft()
            for v in range(self.m):
                if self.adj_matrix[u][v] and self.pair_v[v] == -1:
                    found_augmenting_path = True
                if self.adj_matrix[u][v] and self.pair_v[v] != -1 and self.dist[self.pair_v[v]] == float('inf'):
                    self.dist[self.pair_v[v]] = self.dist[u] + 1
                    queue.append(self.pair_v[v])

        return found_augmenting_path

    def dfs(self, u):
        for v in range(self.m):
            if self.adj_matrix[u][v] and (self.pair_v[v] == -1 or (self.dist[self.pair_v[v]] == self.dist[u] + 1 and self.dfs(self.pair_v[v]))):
                self.pair_u[u] = v
                self.pair_v[v] = u
                return True
        self.dist[u] = float('inf')
        return False

    def hopcroft_karp(self):
        matching_size = 0
        while self.bfs():
            for u in range(self.n):
                if self.pair_u[u] == -1 and self.dfs(u):
                    matching_size += 1
        return matching_size

    def draw_graph(self):
        G = nx.Graph()
        # Добавляем вершины и ребра в граф
        for u in range(self.n):
            for v in range(self.m):
                if self.adj_matrix[u][v]:
                    G.add_edge(f'U{u}', f'V{v}')

        pos = {}
        # Устанавливаем позиции для левой и правой частей
        for i in range(self.n):
            pos[f'U{i}'] = (0, i)  # Левые вершины
        for j in range(self.m):
            pos[f'V{j}'] = (1, j)  # Правые вершины

        # Определяем цвета узлов
        node_colors = ['lightgreen' if i == 0 else 'lightblue' for i in range(self.n)] + ['lightgreen' for _ in range(self.m)]

        nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=2000)
        plt.title("Двудольный граф")
        plt.show()

# Пример использования
if __name__ == "__main__":
    # Новая матрица смежности для двудольного графа
    adj_matrix = [
        [1, 1, 1, 1],
        [1, 0, 0, 1],
        [1, 1, 1, 1],
        [1, 0, 0, 1],
        [1, 1, 1, 1]
    ]

    graph = BipartiteGraph(adj_matrix)
    max_matching = graph.hopcroft_karp()
    print(f"Наибольшее паросочетание: {max_matching}")

    # Отрисовка графа
    graph.draw_graph()
