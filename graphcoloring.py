def is_safe(node, graph, color_assign, color):
    return all(color_assign.get(neigh) != color for neigh in graph[node])

def color_graph(graph, nodes, colors, idx=0, color_assign={}):
    if idx == len(nodes):
        return color_assign
    node = nodes[idx]
    for color in colors:
        if is_safe(node, graph, color_assign, color):
            color_assign[node] = color
            result = color_graph(graph, nodes, colors, idx+1, color_assign)
            if result:
                return result
            color_assign[node] = None
    return None

colors = ['Red', 'Green', 'Blue']

graph1 = {
    'a': ['b','c'],
    'b': ['a','f','e'],
    'c': ['a','d','e'],
    'd': ['c','e'],
    'e': ['b','c','d','z'],
    'f': ['b','z'],
    'z': ['e','f']
}

nodes_graph1 = ['a','b','c','d','e','f','z']
coloring_result = color_graph(graph1, nodes_graph1, colors)

print("Graph 1 Node Coloring:")
for node, color in coloring_result.items():
    print(f"Node {node} -> {color}")
