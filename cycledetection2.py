graph2= {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 3],
    3: [1, 2]
}
def detect_cycle(graph):
    visited = set()

    def dfs_cycle(node, parent):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs_cycle(neighbor, node):
                    return True
            elif neighbor != parent:
                print(f"Cycle detected between {node} and {neighbor}")
                return True
        return False

    for node in graph:
        if node not in visited:
            if dfs_cycle(node, None):
                return
    print("No cycle detected.")

detect_cycle(graph2)
