class Berman_Ford_alghrotim:
    def __init__(self, orientated_graph, starting_node) -> None:
        self.starting_node = starting_node
        self.edges = list(orientated_graph.edges(data = True))
        self.nodes = orientated_graph.nodes
    def shortest_path(self):
        distance = {}
        for v in self.nodes:
            distance[v] = float('inf')
        distance[self.starting_node] = 0
        for i in range(1, len(self.nodes) - 1):
            for edge in self.edges:
                if distance[edge[0]] + edge[2]['weight'] < distance[edge[1]]:
                    distance[edge[1]] = distance[edge[0]] + edge[2]['weight']
        for edge in self.edges:
            if distance[edge[0]] + edge[2]['weight'] < distance[edge[1]]:
                return "Negative cycle detected"
        return {i : j for i, j in distance.items() if j != float('inf')}
berman_ford_result = Berman_Ford_alghrotim(G, 0)
try:
    dist = berman_ford_result.shortest_path()
    for u, w in dist.items():
        print(f"Distance to {u}:", w)
except ValueError:
    print("Negative cycle detected")
