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
           neighbors=[]
           for each_touple in self.graph[key]:
               neighbors.append(each_touple[1][1])
               self.edges[key]=neighbors
    def populate_weights(self):
        for key in self.graph:
            neighbors=self.graph[key]
            for each_tuple in neighbors:
                self.weights[each_tuple[1]]=each_tuple[0]
    def neighbours(self,node):
        return self.edges[node]
    def getcost(self,from_n,to_n):
        return self.weights[(from_n,to_n)]
    def getheuristics(self,node):
        self.heuristic[node]        

    def ucs(graph,start,goal):
        visited=set()
        queue= PriorityQueue()                   