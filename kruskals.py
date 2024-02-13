class kruskal_alghoritm:
    def __init__(self, graph) -> None:
        self.nodes = [[i] for i in graph.nodes]
        self.edges = self.kruskal(list(graph.edges(data = True)), self.nodes)
    @staticmethod
    def find(u, nodes):
        for mn in nodes:
            if u in mn:
                return mn
    def kruskal(self, edges, nodes):
        edges = sorted(edges, key= lambda x : x[2]['weight'])
        edges_tree = []
        for edge in edges:
            if len(nodes) == 1:
                return edges_tree
            vertex1 = kruskal_alghoritm.find(edge[0], nodes)
            vertex2 = kruskal_alghoritm.find(edge[1], nodes)
            if vertex1 != vertex2:
                edges_tree.append((edge[0], edge[1]))
                nodes[nodes.index(vertex2)] += (vertex1)
                nodes.pop(nodes.index(vertex1))
        return edges_tree
