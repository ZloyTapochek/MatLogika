import random
from collections import defaultdict

class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.ROW = len(graph)
        self.COL = len(graph[0])

    def ford_fulkerson(self, source, sink):
        # Create a residual graph
        residual_graph = [[0 for _ in range(self.COL)] for _ in range(self.ROW)]
        for i in range(self.ROW):
            for j in range(self.COL):
                residual_graph[i][j] = self.graph[i][j]

        # Initialize flow to 0
        flow = 0

        while True:
            # Find an augmenting path
            path = self.find_augmenting_path(residual_graph, source, sink)
            if not path:
                break

            # Calculate the minimum capacity along the path
            min_capacity = float('inf')
            for i in range(len(path) - 1):
                min_capacity = min(min_capacity, residual_graph[path[i]][path[i + 1]])

            # Update the flow
            for i in range(len(path) - 1):
                residual_graph[path[i]][path[i + 1]] -= min_capacity
                residual_graph[path[i + 1]][path[i]] += min_capacity

            # Increment the total flow
            flow += min_capacity

        return flow

    def find_augmenting_path(self, residual_graph, source, sink):
        visited = [False for _ in range(self.ROW)]
        parent = [-1 for _ in range(self.ROW)]

        queue = [source]
        visited[source] = True

        while queue:
            u = queue.pop(0)

            for v in range(self.COL):
                if not visited[v] and residual_graph[u][v] > 0:
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u

            if visited[sink]:
                # Construct the path
                path = []
                current = sink
                while current != source:
                    path.append(current)
                    current = parent[current]
                path.append(source)
                path.reverse()
                return path

        return None

    def print_graph(self):
        print("Graph adjacency matrix:")
        for row in self.graph:
            print(" ".join(map(str, row)))

# Create a graph with random weights
graph_size = 25  # Adjust the size of the graph as needed
graph = [[0 for _ in range(graph_size)] for _ in range(graph_size)]

# Generate random weights for the edges
for i in range(graph_size):
    for j in range(graph_size):
        if i != j:
            graph[i][j] = random.randint(1, 10)  # Random weight between 1 and 10

# Set the source and sink nodes
source = 0
sink = graph_size - 1

# Create a graph object
g = Graph(graph)

# Print the graph
g.print_graph()

# Calculate the maximum flow
max_flow = g.ford_fulkerson(source, sink)

# Print the maximum flow
print(f"The maximum flow is: {max_flow}")
