import heapq

def dijkstra(graph, start, end):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    parent = {start: None}
    pq = [(0, start)]

    while pq:
        dist, node = heapq.heappop(pq)
        if node == end:
            path = []
            while node is not None:
                path.append(node)
                node = parent[node]
            return path[::-1], dist
        for neighbor, weight in graph[node]:
            new_dist = dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                parent[neighbor] = node
                heapq.heappush(pq, (new_dist, neighbor))
    return None, float('inf')

graph2 = {
    0: [(1,5),(2,8)],
    1: [(0,5),(2,9),(3,2)],
    2: [(0,8),(1,9),(3,6)],
    3: [(1,2),(2,6)]
}

path, dist = dijkstra(graph2, 0, 3)
print(f"Shortest path from s to t: {path} with distance {dist}")
