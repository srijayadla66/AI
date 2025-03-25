def is_safe(node, color, color_assign, graph):
    return all(color_assign.get(neigh) != color for neigh in graph[node])

def color_graph(graph, nodes, colors, idx=0, color_assign={}):
    if idx == len(nodes):
        return color_assign
    node = nodes[idx]
    for color in colors:
        if is_safe(node, color, color_assign, graph):
            color_assign[node] = color
            result = color_graph(graph, nodes, colors, idx+1, color_assign)
            if result:
                return result
            color_assign[node] = None
    return None

graph2 = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 3],
    3: [1, 2]
}

colors_for_graph2 = ['Yellow', 'Orange', 'Purple']
nodes_graph2 = [0, 1, 2, 3]
coloring_result = color_graph(graph2, nodes_graph2, colors_for_graph2)

print("Graph 2 Node Coloring with different colors:")
for node, color in coloring_result.items():
    print(f"Node {node} -> {color}")
