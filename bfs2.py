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
            "Sibiu": ["Oradea", "Ara": ["Sibiu", "Bucharest"],
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


