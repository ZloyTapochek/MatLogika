import networkx as nx
import matplotlib.pyplot as plt

def draw_graph(G, pos, source, sink):
    # Отрисовка графа
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10, font_weight='bold', arrows=True)
    
    # Указание источника и стока
    plt.text(pos[source][0], pos[source][1] + 0.1, "Источник", fontsize=12, ha='center')
    plt.text(pos[sink][0], pos[sink][1] - 0.1, "Сток", fontsize=12, ha='center')
    
    # Отображение весов на ребрах
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    
    plt.show()

def main():
    # Создание направленного графа
    G = nx.DiGraph()
    
    # Добавление ребер с весами (все веса положительные и конечные)
    G.add_edge('A', 'B', weight=3)
    G.add_edge('A', 'C', weight=2)
    G.add_edge('B', 'C', weight=1)
    G.add_edge('B', 'D', weight=4)
    G.add_edge('C', 'D', weight=2)
    G.add_edge('D', 'E', weight=5)
    
    source = 'A'  # Источник
    sink = 'E'    # Сток
    
    # Вычисление максимального потока
    flow_value, flow_dict = nx.maximum_flow(G, source, sink)
    print(f"Максимальный поток: {flow_value}")
    print("Поток по ребрам:", flow_dict)
    
    # Отрисовка графа
    pos = nx.spring_layout(G)  # Позиции узлов
    draw_graph(G, pos, source, sink)

if __name__ == "__main__":
    main()
