import heapq

def dijkstra(graph, start, target):
    pq = [(0, start)]
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    parent = {start: None}

    while pq:
        curr_distance, curr_node = heapq.heappop(pq)

        if curr_node == target:
            path = []
            while curr_node:
                path.append(curr_node)
                curr_node = parent[curr_node]
            return path[::-1], distances[target]

        for neighbor, weight in graph[curr_node].items():
            distance = curr_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
                parent[neighbor] = curr_node

    return None, float('inf')

graph1 = {
    'a': {'b': 4, 'c': 3},
    'b': {'a': 4, 'f': 5, 'e': 12},
    'c': {'a': 3, 'd': 7, 'e': 10},
    'd': {'c': 7, 'e': 2},
    'e': {'b': 12, 'c': 10, 'd': 2, 'z': 5},
    'f': {'b': 5, 'z': 16},
    'z': {'e': 5, 'f': 16}
}

path, cost = dijkstra(graph1, 'a', 'z')
print(f"Shortest path: {path}, Cost: {cost}")
