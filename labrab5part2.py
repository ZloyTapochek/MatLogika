from collections import defaultdict

def build_bipartite_graph(matrix):
  """Строит двудольный граф из матрицы смежности.

  Args:
    matrix: Матрица смежности, где 1 означает ребро, 0 - отсутствие ребра.

  Returns:
    Словарь, представляющий двудольный граф. Ключи - вершины левой части, 
    значения - списки смежных вершин правой части.
  """
  n_left = len(matrix)
  n_right = len(matrix[0])
  graph = defaultdict(list)
  for i in range(n_left):
    for j in range(n_right):
      if matrix[i][j] == 1:
        graph[i + 1].append(j + 1)  # +1 для удобства нумерации вершин
  return graph

def max_matching(graph):
  """Находит наибольшее паросочетание в двудольном графе.

  Args:
    graph: Словарь, представляющий двудольный граф.

  Returns:
    Список пар вершин, представляющих наибольшее паросочетание.
  """
  matching = {}
  visited = set()
  for u in graph:
    if u not in visited:
      visited.add(u)
      for v in graph[u]:
        if v not in matching or dfs(graph, matching, visited, v):
          matching[u] = v
          break
  return matching

def dfs(graph, matching, visited, v):
  """Рекурсивная функция поиска пути в графе."""
  visited.add(v)
  for u in graph:
    if (u not in matching or matching[u] == v) and u not in visited:
      visited.add(u)
      if (v in graph[u] or not graph[u]):  # Исправленное условие
        if (v not in graph[u] or dfs(graph, matching, visited, matching[u])):
          matching[u] = v
          return True
  return False

matrix = [[1, 1, 1, 1],
         [1, 0, 0, 1],
         [1, 1, 1, 1],
         [1, 0, 0, 1],
         [1, 1, 1, 1]]

graph = build_bipartite_graph(matrix)
matching = max_matching(graph)
print(f"Наибольшее паросочетание: {matching}")