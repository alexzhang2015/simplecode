# 邻接表表示图
from collections import deque
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# DFS


def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for next in set(graph[start]) - visited:
        dfs(graph, next, visited)
    return visited


dfs(graph, 'A')

# BFS


def bfs(graph, start):
    visited = []
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.append(vertex)
            queue.extend(set(graph.get(vertex, [])) - set(visited))
    return visited


bfs(graph, 'A')
