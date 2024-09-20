import networkx as nx
import matplotlib.pyplot as plt

def create_weighted_graph():
    # Создаем направленный граф
    G = nx.DiGraph()

    # Добавляем ребра с весами (пропускной способностью)
    G.add_edge('A', 'B', capacity=10)
    G.add_edge('A', 'C', capacity=5)
    G.add_edge('B', 'C', capacity=15)
    G.add_edge('B', 'D', capacity=10)
    G.add_edge('C', 'D', capacity=10)
    G.add_edge('C', 'E', capacity=5)
    G.add_edge('D', 'E', capacity=10)

    return G

def draw_graph(G):
    pos = nx.spring_layout(G)
    capacities = nx.get_edge_attributes(G, 'capacity')
    nx.draw(G, pos, with_labels=True, node_color='lightblue', arrows=True)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=capacities)
    plt.show()

def max_flow(G, source, sink):
    flow_value, flow_dict = nx.maximum_flow(G, source, sink)
    return flow_value, flow_dict

if __name__ == "__main__":
    # Создаем граф
    G = create_weighted_graph()

    # Отрисовываем граф
    draw_graph(G)

    # Находим максимальный поток
    source = 'A'
    sink = 'E'
    flow_value, flow_dict = max_flow(G, source, sink)

    print(f"Максимальный поток от {source} до {sink}: {flow_value}")
    print("Поток по ребрам:")
    for u, v in flow_dict.items():
        for k, v in v.items():
            print(f"{u} -> {k}: {v}")
