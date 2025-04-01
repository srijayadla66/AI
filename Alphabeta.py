def alpha_beta(curr_node, depth, alpha, beta, is_maximizing, values, path, pruned_nodes):
    if depth == 2:
        return values[curr_node], [curr_node]
    
    if is_maximizing:
        best_value = float('-inf')
        best_path = []
        for child in tree[curr_node]:
            value, child_path = alpha_beta(child, depth + 1, alpha, beta, False, values, path, pruned_nodes)
            if value > best_value:
                best_value = value
                best_path = [curr_node] + child_path
            alpha = max(alpha, best_value)
            if beta <= alpha:
                pruned_nodes.append((curr_node, child))
                break
        return best_value, best_path
    else:
        best_value = float('inf')
        best_path = []
        for child in tree[curr_node]:
            value, child_path = alpha_beta(child, depth + 1, alpha, beta, True, values, path, pruned_nodes)
            if value < best_value:
                best_value = value
                best_path = [curr_node] + child_path
            beta = min(beta, best_value)
            if beta <= alpha:
                pruned_nodes.append((curr_node, child))
                break
        return best_value, best_path

tree = {
    'A': ['B1', 'B2', 'B3'],
    'B1': ['C1', 'C2', 'C3'],
    'B2': ['C4', 'C5', 'C6'],
    'B3': ['C7', 'C8', 'C9']
}

values = {
    'C1': 12, 'C2': 10, 'C3': 3,
    'C4': 5, 'C5': 8, 'C6': 10,
    'C7': 11, 'C8': 2, 'C9': 12
}

pruned_nodes = []
optimal_value, optimal_path = alpha_beta('A', 0, float('-inf'), float('inf'), True, values, [], pruned_nodes)

print("Optimal Path:", ' -> '.join(optimal_path))
print("Optimal Value:", optimal_value)
if pruned_nodes:
    print("Pruned Node:", ', '.join([f"{parent} -> {child}" for parent, child in pruned_nodes]))
else:
    print("No nodes were pruned.")
