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
graph2 = {
            'Oradea': ['Zerind', 'Sibiu'],        
            "Zerind": ["Oradea", "Arad"],
            "Arad": ["Zerind", "Timisoara", "Sibiu"],
            "Timisoara": ["Arad", "Lugoj"],
            "Lugoj": ["Timisoara", "Mehadia"],
            "Mehadia": ["Lugoj", "Dobreta"],
            "Dobreta": ["Mehadia", "Craiova"],
            "Craiova": ["Dobreta", "Rimnicu Vilcea", "Pitesti"],
            "Rimnicu Vilcea": ["Craiova", "Sibiu", "Pitesti"],
            "Sibiu": ["Oradea", "Arad", "Rimnicu Vilcea", "Fagaras"],
            "Fagaras": ["Sibiu", "Bucharest"],
            "Pitesti": ["Craiova", "Rimnicu Vilcea", "Bucharest"],
            "Bucharest": ["Fagaras", "Pitesti", "Giurgiu", "Urziceni"],
            "Giurgiu": ["Bucharest"],
            "Urziceni": ["Bucharest", "Hirsova", "Vaslui"],
            "Hirsova": ["Urziceni", "Eforie"],
            "Eforie": ["Hirsova"],
            "Vaslui": ["Urziceni", "Iasi"],
            "Iasi": ["Vaslui", "Neamt"],
            "Neamt": ["Iasi"]
}

def bfs_connected_component(graph, start,searchvalue):
    # keep track of all visited nodes
    explored = []
    # keep track of nodes to be checked
    queue = [start]


    # keep looping until there are nodes still to be checked
    while queue: 
        # pop the shallowest node (first node) from queue
        node = queue.pop(0)
        if (node==searchvalue):
            explored.append(node)
            return explored
                
        if node not in explored:

                # add node to list of checked nodes
                explored.append(node)
                neighbours = graph[node]
                
                # add neighbours of node to queue
                for neighbour in neighbours:
                    queue.append(neighbour)                
    return []

# Test the function with start node 0
print(bfs_connected_component(graph2,"Arad","Bucharest"))  # Output: [0, 1, 3, 4, 2, 6, 7, 5, 8]
print(bfs_connected_component(graph,0,5)) #Output: [0, 4, 5]