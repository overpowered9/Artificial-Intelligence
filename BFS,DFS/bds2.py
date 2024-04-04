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
def bfs_search(graph,start,searchvalue):
    explored=[]
    openqueue=[start]
    while openqueue:
        node=openqueue.pop(0)
        if node==searchvalue:
            explored.append(node)
            return explored
        if node not in explored:
            explored.append(node)
            neighbors=graph[node]
            openqueue.extend(neighbors)
    return []        
def bfs(gsraph,start):
    explored=[]
    openqueue=[start]
    while openqueue:
        node=openqueue.pop(0)
        if node not in explored:
            explored.append(node)
            neighbors=graph[node]
            openqueue.extend(neighbors)
    return explored     

def dfs(gsraph,start):
    explored=[]
    openqueue=[start]
    while openqueue:
        node=openqueue.pop()
        if node not in explored:
            explored.append(node)
            neighbors=graph[node]
            neighbors.reverse()
            openqueue.extend(neighbors)
    return explored    
# print(bfs_search(graph,0,5)) #Output: [0, 4, 5]
print(dfs(graph,0)) #Output: [0, 1, 2, 5, 4, 7, 8, 3, 6]