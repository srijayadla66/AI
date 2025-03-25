from collections import defaultdict

def add_edge(graph, u, v):
    graph[u].append(v)
    graph[v].append(u)

def detect_cycle_util(graph, node, visited, parent):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            if detect_cycle_util(graph, neighbor, visited, node):
                return True
        elif parent != neighbor:
            return True
    return False

def detect_cycle(graph, nodes):
    visited = {node: False for node in nodes}
    for node in nodes:
        if not visited[node]:
            if detect_cycle_util(graph, node, visited, None):
                return True
    return False

graph = defaultdict(list)
edges = [('a','b'), ('a','c'), ('b','f'), ('b','e'), ('c','d'), ('c','e'), ('d','e'), ('e','z'), ('f','z')]
for u,v in edges:
    add_edge(graph, u, v)

print("Cycle detected in Graph" if detect_cycle(graph, graph.keys()) else "No cycle in Graph")
