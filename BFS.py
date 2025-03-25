from collections import deque

def bfs(start):
    graph = {
        'a': ['b','c'],
        'b': ['a','f','e'],
        'c': ['a','d','e'],
        'd': ['c','e'],
        'e': ['b','c','d','z'],
        'f': ['b','z'],
        'z': ['e','f']
    }
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex, end=" ")
            visited.add(vertex)
            queue.extend(neighbor for neighbor in graph[vertex] if neighbor not in visited)

print("BFS for Graph starting from 'a':")
bfs('a')
