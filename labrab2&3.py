import networkx as nx
import matplotlib.pyplot as plt

def are_graphs_isomorphic(graph1, graph2):
    # Проверяем изоморфность графов
    return nx.is_isomorphic(graph1, graph2)

def draw_graph(graph, title):
    plt.figure()
    pos = nx.spring_layout(graph)  # Определяем расположение узлов
    nx.draw(graph, pos, with_labels=True, node_color='lightblue', node_size=700, font_size=16, font_color='black', font_weight='bold')
    plt.title(title)
    plt.show()

# Пример использования
if __name__ == "__main__":
    # Создаем первый граф
    G1 = nx.Graph()
    G1.add_edges_from([(1, 2), (2, 3), (3, 1), (4,1)])

    # Создаем второй граф
    G2 = nx.Graph()
    G2.add_edges_from([(4, 5), (5, 6), (6, 4)])

    G3 = nx.Graph()
    G3.add_edges_from([(1, 2), (2, 3), (3, 1)])

    # Создаем второй граф
    G4 = nx.Graph()
    G4.add_edges_from([(4, 5), (5, 6), (6, 4)])

    # Проверяем изоморфность
    if are_graphs_isomorphic(G1, G2):
        print("Графы G1 и G2 изоморфны")
    else:
        print("Графы G1 и G2 не изоморфны")
    if are_graphs_isomorphic(G3, G4):
        print("Графы G3 и G4 изоморфны")
    else:
        print("Графы G3 и G4 не изоморфны")
    draw_graph(G1, "Граф 1")
    draw_graph(G2, "Граф 2")
    draw_graph(G3, "Граф 3")
    draw_graph(G4, "Граф 4")

