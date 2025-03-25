def dfs(node, visited=set()):
    graph = {
        'a': ['b','c'],
        'b': ['a','f','e'],
        'c': ['a','d','e'],
        'd': ['c','e'],
        'e': ['b','c','d','z'],
        'f': ['b','z'],
        'z': ['e','f']
    }
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbor in graph[node]:
            dfs(neighbor, visited)

print("\nDFS for Graph starting from 'a':")
dfs('a')
