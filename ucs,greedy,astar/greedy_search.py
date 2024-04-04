from queue import PriorityQueue

class Graph:
    def __init__(self):
        self.graph = {
            # "/": [(0, ("/","A"))],
            "A": [(146, ("A", "O")), (140, ("A", "S")), (494, ("A", "C"))],
            "O": [(146, ("O", "A")), (151, ("O", "S"))],
            "S": [(151, ("S", "O")), (140, ("S", "A")), (80, ("S", "R")), (99, ("S", "F"))],
            "C": [(494, ("C", "A")), (146, ("C", "R"))],
            "R": [(80, ("R", "S")), (146, ("R", "C")), (97, ("R", "P"))],
            "F": [(99, ("F", "S")), (211, ("F", "B"))],
            "B": [(211, ("B", "F")), (101, ("B", "P"))],
            "P": [(101, ("P", "B")), (97, ("P", "R")), (138, ("P", "C"))]
        }

        self.edges = {}
        self.weights = {}
        self.heuristic = {
            "A": 10,
            "O": 9,
            "S": 7,
            "C": 8,
            "R": 6,
            "F": 5,
            "P": 3,
            "B": 0
        }

    def populate_edges(self):
        for key in self.graph:
            neighbours = []
            for each_tuple in self.graph[key]:
                neighbours.append(each_tuple[1][1])

            self.edges[key] = neighbours

    def populate_weights(self):
        for key in self.graph:
            neighbours = self.graph[key]
            for each_tuple in neighbours:
                self.weights[each_tuple[1]] = each_tuple[0]

    def neighbors(self, node):
        return self.edges[node]

    def get_cost(self, from_node, to_node):
        return self.weights[(from_node,  to_node)]

    def get_heuristic(self, node):
        return self.heuristic[node]


def a_star(graph, start, goal):
    visited = set()
    queue = PriorityQueue()
    queue.put((0 + graph.get_heuristic(start), start))  # Include heuristic for the start node
    parent = {start: (None, 0)}  # To store parent nodes and cumulative cost for path reconstruction
    
    while not queue.empty():
        cost, node = queue.get()
        
        if node not in visited:
            visited.add(node)
            
            if node == goal:
                # Reconstruct the path from start to goal
                path = []
                while node is not None:
                    path.append(node)
                    node = parent[node][0]
                return path[::-1], parent[goal][1]  # Return the path in correct order and total cost
            
            for n in graph.neighbors(node):
                if n not in visited:
                    total_cost = cost + graph.get_cost(node, n) + graph.get_heuristic(n)  # Include heuristic in total cost
                    queue.put((total_cost, n))
                    parent[n] = (node, total_cost)  # Update parent and cumulative cost for node n
    
    return [], float('inf')  # Goal not reachable, return an empty path and infinite cost




def ucs(graph, start, goal):
    visited = set()
    queue = PriorityQueue()
    queue.put((0, start))
    # dictionary to keep track of the parent node and the cost for each visited node
    parent = {start: (None, 0)}
    
    while not queue.empty():
        cost, node = queue.get()
        
        if node not in visited:
            visited.add(node)
            
            if node == goal:
                # Reconstruct the path from start to goal
                path = []
                while node is not None:
                    path.append(node)
                    node = parent[node][0]
                return path[::-1], parent[goal][1]  # Return the path and total cost
                
            for n in graph.neighbors(node):
                if n not in visited:
                    total_cost = cost + graph.get_cost(node, n)
                    queue.put((total_cost, n))
                    # Update parent for node n and the cost
                    parent[n] = (node, total_cost)
                    print(f"Parent: {parent}")
    
    return [], float('inf')  # Goal not reachable, return an empty path and infinite cost



def greedy_best_first_search(graph, start, goal):
    visited = set()
    queue = PriorityQueue()
    queue.put((0, start))
    parent = {start: None}  # To store parent nodes for path reconstruction
    
    while not queue.empty():
        _, node = queue.get()
        
        if node not in visited:
            visited.add(node)
            if node == goal:
                # Reconstruct the path from start to goal
                path = []
                while node is not None:
                    path.append(node)
                    node = parent[node]
                return path[::-1]  # Return the path in correct order
            
            for n in graph.neighbors(node):
                if n not in visited:
                    priority = graph.get_heuristic(n)  # Greedy Best-First Search uses heuristic as priority
                    queue.put((priority, n))
                    parent[n] = node  # Update parent for node n
    
    return []  # Goal not reachable


graph = Graph()
graph.populate_edges()
graph.populate_weights()
print("edges    : ", graph.edges)
print("weights  : ", graph.weights)
print("heristics: ", graph.heuristic)
print("UCS       : ", ucs(graph, "A", "B"))
# print("A*       : ", a_star(graph, "A", "B"))
# print("GBFS     : ", greedy_best_first_search(graph, "A", "B"))