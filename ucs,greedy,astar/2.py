from queue import PriorityQueue
class Graph:
    def __init__(self):
        self.graph = {
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
graph = Graph()
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
    return [], float('inf')    
def greedy_search(graph,start,end):
    visited=set()
    queue=PriorityQueue()
    queue.put((0,start))
    parent={start:None}
    while not queue.empty():
        ok,node=queue.get()
        if node not in visited:
            visited.add(node)
            if node==end:
                path=[]
                while node is not None:
                    path.append(node)
                    node=parent[node]
                    
                return path[::-1]
            for n in graph.neighbors(node):
              if n not in visited:
                heuristics=graph.get_heuristic(n)
                queue.put((heuristics,n))
                parent[n]=node
    return ['1']            

def astar(graph,start,end):
    visited=set()
    queue=PriorityQueue()
    queue.put((graph.get_heuristic(start),(start,0)))
    parent={start:(None,0)}
    while not queue.empty():
        _,(node,cost)=queue.get()
        if node not in visited:
            visited.add(node)
            if node==end:
                path=[]
                while node is not None:
                    path.append(node)
                    node=parent[node][0]
                return path[::-1], parent[end][1]
            for n in graph.neighbors(node):
                if n not in visited:
                    cost_gn=cost+graph.get_cost(node,n)
                    total_cost=graph.get_heuristic(n)+cost_gn
                    queue.put((total_cost,(n,cost_gn)))
                    parent[n]=(node,total_cost)



    


graph.populate_edges()
graph.populate_weights()
graph.get_heuristic


# print("edges    : ", graph.edges)
# print("weights  : ", graph.weights)
# print("heristics: ", graph.heuristic)
print("UCS" ,astar(graph, "A", "B"))