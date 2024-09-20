import networkx as nx
import matplotlib.pyplot as plt
import heapq


def dijkstra(graph, start):
    # Инициализация расстояний и приоритетной очереди
    distances = {node: float('infinity') for node in graph.nodes}
    distances[start] = 0
    priority_queue = [(0, start)]  # (расстояние, узел)

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Узел уже обработан с меньшим расстоянием
        if current_distance > distances[current_node]:
            continue

        # Обход соседей
        for neighbor in graph.neighbors(current_node):
            weight = graph[current_node][neighbor]['weight']
            distance = current_distance + weight

            # Если найдено более короткое расстояние
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances
def draw_graph(graph):
    pos = nx.spring_layout(graph)  # Определяем расположение узлов
    plt.figure()

    # Рисуем узлы
    nx.draw(graph, pos, with_labels=True, node_color='lightblue', node_size=700, font_size=16, font_color='black', font_weight='bold')

    # Рисуем рёбра с весами
    edge_labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_color='red', font_size=12)

    plt.title("Граф с весами рёбер")
    plt.show()

# Пример использования
if __name__ == "__main__":
    # Создаем граф
    G = nx.Graph()
    G.add_weighted_edges_from([ #Первая вершина, вторая вершина, вес ребра
        (1, 2, 3), #От первого до второго узла
        (1, 3, 4), #От первого до третьего узла
        (2, 3, 2), #От второго до третьего узла
        (2, 4, 5), #От второго до четвертого узла
        (3, 4, 1)  #От третьего до четвертого узла
    ])

    start_node = 1
    distances = dijkstra(G, start_node)

    print(f"Кратчайшие расстояния от узла {start_node}:")
    for node, distance in distances.items():
        print(f"До узла {node}: {distance}")

    # Визуализируем граф
    draw_graph(G)
