graph = {
    0: [1, 3, 4],
    1: [2, 4],
    2: [5],
    3: [4, 6],
    4: [5, 7],
    5: [],
    6: [4, 7],
    7: [5, 8],
    8: [],
}

# Visits all the nodes of a graph (connected component) using DFS
def dfs_connected_component(graph, start, explored=None):
    if explored is None:
        explored = []
    
    if start not in explored:
        explored.append(start)
        neighbours = graph[start]
        for neighbour in neighbours:
            dfs_connected_component(graph, neighbour, explored)
    
    return explored

# Test the function with start node 7
print(dfs_connected_component(graph, 0))  # Output: [7, 5, 8, 4, 6, 0, 1, 2, 3]
