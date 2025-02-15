def greedy(adj_list, heuristics, start):
    current = start
    path = [current]  
    while heuristics[current] != 0:
        min_h=float('inf')
        next_node=-1
        
        for neighbor, _ in adj_list[current]:
            if heuristics[neighbor] < min_h:
                min_h = heuristics[neighbor]
                next_node = neighbor
        
        if next_node == -1:
            return "Goal Node Not Found"
        
        current = next_node
        path.append(current)
    
    return f"Goal found at node {current} with path: {path}"
list = {
    0: [(1,3), (2,2)],
    1: [(3,4), (4,1)],
    2: [(5,3), (6,1)],
    3: [],
    4: [],
    5: [(8,5)],
    6: [(7,3), (9,2)],
    7: [],
    8: [],
    9: []
}
heuristics = [13,12,4,7,2,8,2,0,4,9]
start=0
result=greedy(list, heuristics, start)
print(result)
